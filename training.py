import torch
import cnn
import torch.optim as optim
import torch.nn as nn


def train(train_set):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    batch_size = 4
    num_workers = 2
    learning_rate = 0.001
    momentum = 0.9
    num_epochs = 2

    train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=num_workers)

    net = cnn.Net().to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=learning_rate, momentum=momentum)

    for epoch in range(num_epochs):

        for i, (inputs, labels) in enumerate(train_loader):

            inputs = inputs.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

    epoch_loss = 0.0

    for j, (inputs, labels) in enumerate(train_loader):
        inputs = inputs.to(device)
        labels = labels.to(device)

        outputs = net(inputs)
        loss = criterion(outputs, labels)

        epoch_loss += loss.item()

    print('Finished Training')
    print(f'Loss: {epoch_loss / j}\n')

    PATH = './mnist_net.pth'
    torch.save(net.state_dict(), PATH)

    return epoch_loss / j
