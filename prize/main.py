import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

def lottery_simulation(prize_one, prize_two, prize_three, prize_four, prize_zero, prize_num):
    # 初始奖品数量
    initial_prizes = {
        'one': prize_one,
        'two': prize_two,
        'three': prize_three,
        'four': prize_four,
        'zero': prize_zero
    }

    # 当前奖品数量
    current_prizes = initial_prizes.copy()

    # 总票数
    total_tickets = sum(initial_prizes.values())

    for _ in range(prize_num):
        if total_tickets <= 0:
            break

        # 随机抽取
        draw = random.randint(1, total_tickets)
        current_total = 0

        for prize, amount in current_prizes.items():
            current_total += amount
            if draw <= current_total:
                current_prizes[prize] -= 1
                total_tickets -= 1
                break

    # 计算剩余奖品的百分比
    remaining_percentages = {
        prize: (current_prizes[prize] / initial_prizes[prize]) * 100
        for prize in ['one', 'two', 'three', 'four']
        if initial_prizes[prize] > 0
    }

    return remaining_percentages

def total_remaining_percentage(initial_prizes, current_prizes):
    # 计算总未抽走的奖品数量
    total_remaining = sum(current_prizes.values())
    # 计算总奖品数量
    total_initial = sum(initial_prizes.values())
    # 计算未抽走占总奖品的比例
    return (total_remaining / total_initial)

def average_remaining_percentage(prize_one, prize_two, prize_three, prize_four, prize_zero, prize_num, simulations):
    total_percentage = 0

    # 初始奖品数量
    initial_prizes = {
        'one': prize_one,
        'two': prize_two,
        'three': prize_three,
        'four': prize_four,
        'zero': prize_zero
    }

    for _ in range(simulations):
        # 进行一次模拟
        current_prizes = lottery_simulation(prize_one, prize_two, prize_three, prize_four, prize_zero, prize_num)
        # 计算未抽走占总奖品的比例
        percentage = total_remaining_percentage(initial_prizes, current_prizes)
        total_percentage += percentage

    # 计算平均百分比
    return total_percentage / simulations

def simulate_with_varying_prize_zero(prize_one, prize_two, prize_three, prize_four, prize_num, start_zero, end_zero):
    x_values = []  # prize_zero 的值
    y_values = []  # 对应的剩余奖品比例

    # 遍历不同的 prize_zero 值
    for prize_zero in range(start_zero, end_zero + 1):
        # 进行一次模拟
        current_prizes = lottery_simulation(prize_one, prize_two, prize_three, prize_four, prize_zero, prize_num)
        initial_prizes = {'one': prize_one, 'two': prize_two, 'three': prize_three, 'four': prize_four, 'zero': prize_zero}
        # 计算未抽走占总奖品的比例
        percentage = total_remaining_percentage(initial_prizes, current_prizes)

        # 记录结果
        x_values.append(prize_zero)
        y_values.append(percentage)

    return x_values, y_values

def simulate_3d(prize_one, prize_two, prize_three, prize_four, start_zero, end_zero, start_num, end_num, simulations):
    x_values, y_values, z_values = [], [], []

    for prize_zero in range(start_zero, end_zero + 1):
        for prize_num in range(start_num, end_num + 1):
            # 计算平均剩余奖品比例
            avg_percentage = average_remaining_percentage(prize_one, prize_two, prize_three, prize_four, prize_zero,
                                                          prize_num, simulations)

            # 记录结果
            x_values.append(prize_zero)
            y_values.append(prize_num)
            z_values.append(avg_percentage)

    return x_values, y_values, z_values






# 设置奖品数量
prize_one = 2
prize_two = 25
prize_three = 59
prize_four = 48
prize_zero = 2000  # 参与奖
prize_num = 1200  # 抽奖次数
simulations = 10  # 重复模拟次数


# 进行模拟
x_values, y_values, z_values = simulate_3d(prize_one, prize_two, prize_three, prize_four, 500, 1000, 600, 1000, simulations)


# 绘制3D图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_values, y_values, z_values, c=z_values, cmap='viridis')
ax.set_xlabel('参与奖数量')
ax.set_ylabel('抽奖次数')
ax.set_zlabel('平均剩余奖品比例')
plt.title('平均剩余奖品比例 与 参与奖数量 和 抽奖次数关系图')
plt.show()


