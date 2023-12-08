# 逻辑斯蒂回归

import torch
import numpy as np
import matplotlib.pyplot as plt

x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[0], [0], [1]])


class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LogisticRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred


model = LogisticRegressionModel()
# 构造损失函数
# BCELoss 二元交叉熵损失 用于二元分类任务
criterion = torch.nn.BCELoss(size_average=False)
# 构造优化器
# Adam算法 自适应学习率 动量优化 Bias修正 超参数调整
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(100):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.item())
    # 清除梯度
    optimizer.zero_grad()
    # 梯度反向传播
    loss.backward()
    # 自动更新学习率等参数
    optimizer.step()

x = np.linspace(0, 10, 200)  # 0-10区间，取200个点
x_t = torch.Tensor(x).view((200, 1))  # .view()函数类似reshape()
y_t = model(x_t)
y = y_t.data.numpy()  # 得到数组

plt.title("Optimizer = SGD")
plt.plot(x, y)
plt.plot([0, 10], [0.5, 0.5], c='r')
plt.xlabel('Hours')
plt.ylabel('Probability of Pass')
plt.grid()  # 设置网格线
plt.show()