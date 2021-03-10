import checks


def find_leaves_pairs(pairs_s_list):
    leaves_pairs = []

    pairs_sorted_list = [[] for i in range(len(pairs_s_list[0]))]

    for i in range(4):
        for (j, p) in enumerate(pairs_s_list[i]):
            pairs_sorted_list[j].append(p)

    leaves_pairs.append(pairs_sorted_list[0][0])
    for i in range(1, 4, 1):
        k = 0
        check = checks.check_duplicate(pairs_sorted_list[k][i], leaves_pairs)
        if not check:
            leaves_pairs.append(pairs_sorted_list[k][i])
        else:
            while check:
                k += 1
                check = checks.check_duplicate(pairs_sorted_list[k][i], leaves_pairs)
            leaves_pairs.append(pairs_sorted_list[k][i])

    for i in range(4):
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

    i = 2
    j = 0
    l = 4

    print(leaves_pairs)

    while not checks.check_all_true(digits):
        added = False
        while not added:
            pair = pairs_sorted_list[i][j]
            if checks.check_how_many(digits) <= 2:
                for k in range(2):
                    if not digits[pair[k][0]]:
                        leaves_pairs[l] = pair
                        print(leaves_pairs)
                        if l < 6:
                            l += 1
                        else:
                            l = 0
                        added = True
                        for i in digits:
                            digits[i] = checks.check_digit(i, leaves_pairs)
            elif (not digits[pair[0][0]]) and (not digits[pair[1][0]]):
                leaves_pairs[l] = pair
                print(leaves_pairs)
                if l < 6:
                    l += 1
                else:
                    l = 0
                added = True
                for i in digits:
                    digits[i] = checks.check_digit(i, leaves_pairs)
            if j < 3:
                j += 1
                print(j)
            else:
                j = 0
                if i == 44:
                    i = 0
                i += 1
                print(j, i)

    print(leaves_pairs)
