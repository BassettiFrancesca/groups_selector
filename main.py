import sort_pairs
import find_leaves_pairs


def print_groups():
    pairs_train_list = []
    pairs_test_list = []

    for i in range(4):
        (train, test) = sort_pairs.sort_pairs()
        pairs_train_list.append(train)
        pairs_test_list.append(test)

    find_leaves_pairs.find_leaves_pairs(pairs_train_list)

    find_leaves_pairs.find_leaves_pairs(pairs_test_list)


if __name__ == '__main__':
    print_groups()

