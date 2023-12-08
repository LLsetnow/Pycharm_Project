# pytorch自动梯度计算 反向传播
import torch
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]


w = torch.Tensor([1.0])  # 初始权值
w.requires_grad = True  # 需要计算梯度，默认不更新


def forward(x):
    return x * w  # Tensor(x)自动类型转换将x转成Tensor


def loss(x, y):  # 每调用一次loss函数，动态构建一次计算图，而非进行一次乘方运算
    y_pred = forward(x)
    return (y_pred - y) ** 2


epoch_list = []
l_list = []

print("predict(before training):", 4, forward(4).item())

# w.data      张量 w 的数据值 提供对数据的直接访问
# w.grad.data 张量 w 的梯度数据值
# 每次epoch自动计算出梯度 并存储在w.grad
for epoch in range(100):
    for x, y in zip(x_data, y_data):
        l = loss(x, y)  # 前向传播计算张量，使用张量构建计算图
        l.backward()  # 每调用一次backward()，形成一张计算图，自动求出计算图中所有梯度，存入变量中，随即释放该计算图(Pytorch特点)
        print('\tgrad:', x, y, w.grad.item())  # 将梯度中的数值直接取出成为一个标量
        w.data = w.data - 0.01 * w.grad.data  # 使用梯度的data更新权重，若直接使用梯度，则会构建计算图

        w.grad.data.zero_()  # 梯度权重数据清零，否则下一次的权重会在新计算出的权重基础上加上上次的权重
    print("progress:", epoch, l.item())   # 提取 l 张量的标量（loss值）
    epoch_list.append(epoch)
    l_list.append(l.item())

# 不可sum+=l,l为张量,sum为标量，上式使计算图不断扩大可能最终耗尽内存，应为sum+=l.item()

print("predict(after training):", 4, forward(4).item())

plt.plot(epoch_list, l_list)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()