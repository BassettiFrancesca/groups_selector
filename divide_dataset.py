import torch
import torchvision
import torchvision.transforms as transforms
import GroupDataset


def divide_dataset(groups):

    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    train_set = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_set, shuffle=False, num_workers=2)

    test_set = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    test_loader = torch.utils.data.DataLoader(test_set, shuffle=False, num_workers=2)

    indices = []

    for i, (image, label) in enumerate(train_loader):
        for j in range(len(groups)):
            if label[0] in groups[j]:
                indices.append(i)

    indices.sort()

    node_dataset = torch.utils.data.Subset(train_set, indices)

    train_node_dataset = GroupDataset.GroupDataset(node_dataset, groups)

    print(f'Size leaf_dataset {groups}: {len(train_node_dataset)}')

    test_indices = []

    for i, (image, label) in enumerate(test_loader):
        for j in range(len(groups)):
            if label[0] in groups[j]:
                test_indices.append(i)

    test_data_set = torch.utils.data.Subset(test_set, test_indices)

    test_new_dataset = GroupDataset.GroupDataset(test_data_set, groups)

    print(f'Size test_leaf_dataset {groups}: {len(test_new_dataset)}\n')

    return train_node_dataset, test_new_dataset
