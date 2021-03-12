import find_leaves_pairs
import sort_pairs


def find_leaves():
    pairs_train_list = []
    pairs_test_list = []
    run = 4

    for i in range(run):
        print(f'Run {i}\n')
        (train, test) = sort_pairs.sort_pairs()
        pairs_train_list.append(train)
        pairs_test_list.append(test)

    print('Finding leaves with loss:\n')

    find_leaves_pairs.find_leaves_pairs(pairs_train_list, run)

    print('')

    print('Finding leaves with accuracy:\n')

    find_leaves_pairs.find_leaves_pairs(pairs_test_list, run)
