import divide_dataset
import training
import testing


def sort_pairs():
    digits = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    pairs = []

    for i in range(len(digits)):
        for j in range(i + 1, len(digits), 1):
            pairs.append([digits[i], digits[j]])

    accuracy_pairs_test = {}
    loss_pairs_train = {}

    for pair in pairs:
        (train_set, test_set) = divide_dataset.divide_dataset(pair)
        loss = training.train(train_set)
        accuracy = testing.test(test_set)
        accuracy_pairs_test[accuracy] = pair
        loss_pairs_train[loss] = pair

    pairs_sorted_train = []
    pairs_sorted_test = []

    for i in sorted(accuracy_pairs_test):
        pairs_sorted_test.append(accuracy_pairs_test[i])

    for i in sorted(loss_pairs_train):
        pairs_sorted_train.append(loss_pairs_train[i])

    pairs_sorted_train.reverse()

    print(pairs_sorted_test)
    print(pairs_sorted_train)

    return pairs_sorted_train, pairs_sorted_test

