import checks
import divide_dataset
import training


def find_nodes1():
    leaves = [[[5], [8]], [[7], [9]], [[3], [9]], [[0], [8]], [[1], [4]], [[1], [6]], [[8], [9]], [[2], [9]]]

    for i in range(len(leaves)):
        for j in range(len(leaves[i])):
            leaves[i][j] = leaves[i][j][0]

    pairs_leaves = []

    for i in range(len(leaves)):
        for j in range(i + 1, len(leaves), 1):
            pairs_leaves.append([leaves[i], leaves[j]])

    loss_pairs_train = {}
    pairs_loss = []

    for pair in pairs_leaves:
        (train_set, test_set) = divide_dataset.divide_dataset(pair)
        loss = training.train(train_set)
        pair = str(pair)
        loss_pairs_train[pair] = loss
        pairs_loss.append(loss)

    pairs_loss.sort()
    pairs_loss.reverse()
    pairs_sorted_train = []

    for l in pairs_loss:
        key = checks.find_key(loss_pairs_train, l)
        pairs_sorted_train.append(checks.str_to_pair(key, pairs_leaves))

    print(pairs_sorted_train)

    found = {}

    for i in leaves:
        found[str(i[0]) + '-' + str(i[1])] = False

    nodes = []

    i = 0

    while not checks.check_all_true(found):
        leaves = pairs_sorted_train[i]
        if (not found[str(leaves[0][0]) + '-' + str(leaves[0][1])]) and (
                not found[str(leaves[1][0]) + '-' + str(leaves[1][1])]):
            found[str(leaves[0][0]) + '-' + str(leaves[0][1])] = True
            found[str(leaves[1][0]) + '-' + str(leaves[1][1])] = True
            nodes.append(leaves)
        i += 1

    print(nodes)
