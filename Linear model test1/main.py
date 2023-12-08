import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

matplotlib.use('TkAgg')

# y=w*x+b
# 此处设为 y = 2 * x + 3
x_data = [1.0, 2.0, 3.0]
y_data = [5.0, 7.0, 9.0]


def forward(x):
    return w * x + h


def loss(x, y):  # MSE
    y_pred = forward(x)
    return (y - y_pred) ** 2


mse_list = []  # 对应w权重的MSE
W = np.arange(0, 5, 0.1)  # 一维数组
H = np.arange(0, 7, 0.1)  # 一维数组

# [w,b]=np.meshgrid(W,B) 函数用两个坐标轴上的点在平面上画网格。
[w, h] = np.meshgrid(W, H)      # 二维数组 W * H  [w, h]为一个点的坐标


# w.ravel() 将w以一维数组返回
# for x, y in zip(w.ravel(), h.ravel()):
#     # 计算x和y
#     x_val = x % 3
#     y_val = y % 4
#     # 打印网格上每一个点坐标
#     print("point = [{}, {}]".format(x_val, y_val))

# 没懂怎么实现遍历的
l_sum = 0
for x_val, y_val in zip(x_data, y_data):
    y_pre_val = forward(x_val)
    # print(y_pre_val)
    loss_val = loss(x_val, y_val)
    l_sum += loss_val

fig = plt.figure()
ax = Axes3D(fig)  # Axes3D是mpl_toolkits.mplot3d中的一个绘图函数
# 设置坐标轴的值
ax.plot_surface(w, h, l_sum / 3)  # 画曲面图---Axes3D.plot_surface(X, Y, Z)
# 设置坐标轴名称
ax.set_xlabel("W")
ax.set_ylabel("B")
ax.set_zlabel("Cost Value")
plt.show()