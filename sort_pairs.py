import checks
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
    pairs_accuracy = []
    pairs_loss = []

    for pair in pairs:
        (train_set, test_set) = divide_dataset.divide_dataset(pair)
        loss = training.train(train_set)
        accuracy = testing.test(test_set)
        pair = str(pair)
        accuracy_pairs_test[pair] = accuracy
        pairs_accuracy.append(accuracy)
        loss_pairs_train[pair] = loss
        pairs_loss.append(loss)

    pairs_accuracy.sort()
    pairs_sorted_test = []

    for a in pairs_accuracy:
        key = checks.find_key(accuracy_pairs_test, a)
        pairs_sorted_test.append(checks.str_to_pair(key, pairs))

    pairs_loss.sort()
    pairs_loss.reverse()
    pairs_sorted_train = []

    for l in pairs_loss:
        key = checks.find_key(loss_pairs_train, l)
        pairs_sorted_train.append(checks.str_to_pair(key, pairs))

    print(f'Pairs_sorted_train: {pairs_sorted_train}\n')
    print(f'Pairs_sorted_test: {pairs_sorted_test}\n')

    return pairs_sorted_train, pairs_sorted_test

