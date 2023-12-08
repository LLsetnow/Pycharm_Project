# 梯度下降 线性回归示例，用于拟合一个线性模型（y = wx）
import matplotlib
import matplotlib.pyplot as plt

matplotlib.get_backend()

x_data = [1.0, 2.0, 3.0, 4.0]
y_data = [2.0, 4.0, 6.0, 8.0]
w = 1.0


def forward(x):
    return x * w


# 计算模型的均方误差（MSE）损失
def cost(xs, ys):
    cost = 0
    for x, y in zip(xs, ys):
        y_pred = forward(x)
        cost += (y - y_pred) ** 2
    return cost / len(xs)


# 计算损失函数对权重w的梯度。使用 MSE 损失函数的导数，它将遍历输入特征xs和对应的目标值ys，计算每个样本的梯度，然后求平均
def gradient(xs, ys):
    grad = 0
    for x, y in zip(xs, ys):
        grad += 2 * x * (w * x - y)
    return grad / len(xs)


print("Predict(before training)", 4, forward(4))

# 记录每步的均方误差（MSE）
cost_list = []
# 记录当前步数
epoch_list = []

# 对w梯度下降 寻找损失函数最小值
for epoch in range(100):
    cost_val = cost(x_data, y_data)
    grad_val = gradient(x_data, y_data)
    # -= 求反向梯度
    w -= 0.1 * grad_val
    cost_list.append(cost_val)
    epoch_list.append(epoch)
    print("Epoch:", epoch, " w=", w, " loss=", cost_val)

print("Predict(after training)", 5, forward(5))

plt.plot(epoch_list, cost_list)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()
