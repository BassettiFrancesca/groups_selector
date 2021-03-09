import divide_dataset
import training
import testing


def find_leaves(num_leaves):
    digits = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    pairs = []

    for i in range(len(digits)):
        for j in range(i + 1, len(digits), 1):
            pairs.append([digits[i], digits[j]])

    accuracy_pairs = {}

    for pair in pairs:
        (train_set, test_set) = divide_dataset.divide_dataset(pair)
        training.train(train_set)
        accuracy = testing.test(test_set)
        accuracy_pairs[accuracy] = pair

    pairs_sorted = []

    for i in sorted(accuracy_pairs):
        pairs_sorted.append(accuracy_pairs[i])

    print(pairs_sorted)

    return pairs_sorted

