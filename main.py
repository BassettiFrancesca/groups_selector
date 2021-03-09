import find_leaves
import check_digit
import check_all_true


def print_groups():
    pairs_sorted_list = []
    leaves_pairs = []
    for i in range(4):
        pairs_sorted_list.append(find_leaves.find_leaves(8))
        leaves_pairs.append(pairs_sorted_list[i][0])

    digits = {}

    for i in range(10):
        digits[i] = False

    for i in digits:
        digits[i] = check_digit.check_digit(i, leaves_pairs)

    i = 0

    while (not check_all_true.check_all_true(digits)) or (len(leaves_pairs) < 8):
        added = False
        while not added:
            k = 1
            pair = pairs_sorted_list[i][k]
            done = False
            if not check_all_true.check_all_true(digits):
                while not done:
                    for i in range(2):
                        real = digits[pair[i][0]]
                        digits[pair[i][0]] = True
                        if check_all_true.check_all_true(digits):
                            digits[pair[i][0]] = real
                            if not digits[pair[i][0]]:
                                leaves_pairs.append(pair)
                                real = True
                                done = True
                                added = True
                        digits[pair[i][0]] = real
                    if (not digits[pair[0][0]]) and (not digits[pair[1][0]]):
                        leaves_pairs.append(pair)
                        done = True
                        added = True
                        digits[pair[0][0]] = True
                        digits[pair[1][0]] = True
                    elif not done:
                        k += 1
                        pair = pairs_sorted_list[i][k]

            else:
                leaves_pairs.append(pair)
                added = True
        i += 1

    print(leaves_pairs)


if __name__ == '__main__':
    print_groups()
