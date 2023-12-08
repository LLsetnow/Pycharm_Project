import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

# 前向传播
def forward(x):
    return x * w


def loss(x, y):  # MSE
    y_pred = forward(x)
    return (y - y_pred) ** 2


w_list = []  # 权重
mse_list = []  # 对应权重损失值

# 数组内的值 >= 起始值  < 中止值
# np.arange(起始值, 中止值, 步长):
for w in np.arange(0.0, 4.1, 0.1):
    print('w=', w)
    l_sum = 0
    # 从x_data,y_data中取出数据，用zip拼成x_val,y_val
    for x_val, y_val in zip(x_data, y_data):
        y_pre_val = forward(x_val)  # 该变量设置目的为打印预测值
        loss_val = loss(x_val, y_val)
        l_sum += loss_val
        print('\t', x_val, y_val, y_pre_val, loss_val)
    # 平均平方误差
    print("MSE=", l_sum / 3, "\r\n")
    # 向列表w_list添加元素
    w_list.append(w)
    mse_list.append(l_sum / 3)

# 画图
plt.plot(w_list, mse_list)     # w_list为x轴数据 mse_list为y轴
plt.ylabel('Loss')                   # y轴标签
plt.xlabel('w')                      # x轴标签
plt.show()                           # 显示图形