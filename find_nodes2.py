import checks
import divide_dataset
import training


def find_nodes2():
    nodes1 = [[1, 6, 2, 9], [5, 8, 8, 9], [3, 9, 0, 8], [7, 9, 1, 4]]

    pairs_leaves = []

    for i in range(len(nodes1)):
        for j in range(i + 1, len(nodes1), 1):
            pairs_leaves.append([nodes1[i], nodes1[j]])

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

    for i in nodes1:
        found[str(i)] = False

    nodes = []

    i = 0

    while not checks.check_all_true(found):
        node = pairs_sorted_train[i]
        if (not found[str(node[0])]) and (not found[str(node[1])]):
            found[str(node[0])] = True
            found[str(node[1])] = True
            nodes.append(node)
        i += 1

    print(nodes)
