import checks


def find_leaves_pairs(pairs_s_list, run):
    leaves_pairs = []

    pairs_sorted_list = [[] for i in range(len(pairs_s_list[0]))]

    for i in range(run):
        for (j, p) in enumerate(pairs_s_list[i]):
            pairs_sorted_list[j].append(p)

    leaves_pairs.append(pairs_sorted_list[0][0])
    for i in range(1, run, 1):
        k = 0
        check = checks.check_duplicate(pairs_sorted_list[k][i], leaves_pairs)
        if not check:
            leaves_pairs.append(pairs_sorted_list[k][i])
        else:
            while check:
                k += 1
                check = checks.check_duplicate(pairs_sorted_list[k][i], leaves_pairs)
            leaves_pairs.append(pairs_sorted_list[k][i])

    for i in range(run):
        k = 1
        check = checks.check_duplicate(pairs_sorted_list[k][i], leaves_pairs)
        if not check:
            leaves_pairs.append(pairs_sorted_list[k][i])
        else:
            while check:
                k += 1
                check = checks.check_duplicate(pairs_sorted_list[k][i], leaves_pairs)
            leaves_pairs.append(pairs_sorted_list[k][i])

    digits = {}

    for i in range(10):
        digits[i] = False

    for i in digits:
        digits[i] = checks.check_digit(i, leaves_pairs)

    index = 2
    j = 0
    l = 4

    counter = 0

    print(f'leaves_pairs: {leaves_pairs}  counter: {counter}\n')

    while not checks.check_all_true(digits):
        added = False
        while not added:
            pair = pairs_sorted_list[index][j]
            print(pair, index, j, l)
            if checks.check_how_many(digits) <= 2:
                for k in range(2):
                    if not digits[pair[k][0]]:
                        leaves_pairs[l] = pair
                        index = 1
                        j = -1
                        counter += 1
                        print(f'leaves_pairs: {leaves_pairs}  counter: {counter}\n')
                        if l <= 7:
                            l += 1
                            if l == 8:
                                l = 4
                        added = True
                        for d in digits:
                            digits[d] = checks.check_digit(d, leaves_pairs)
                        print(digits)
                        print('')
            elif (not digits[pair[0][0]]) and (not digits[pair[1][0]]):
                leaves_pairs[l] = pair
                index = 1
                j = -1
                counter += 1
                print(f'leaves_pairs: {leaves_pairs}  counter: {counter}\n')
                if l <= 7:
                    l += 1
                    if l == 8:
                        l = 4
                added = True
                for d in digits:
                    digits[d] = checks.check_digit(d, leaves_pairs)
                print(digits)
                print('')
            if j < 3:
                j += 1
            else:
                j = 0
                index += 1
                if index == 45:
                    index = 1

    print('')

    print('Final leaves_pairs:\n')

    print(f'leaves_pairs: {leaves_pairs}  counter: {counter}\n')
