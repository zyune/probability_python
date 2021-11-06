import numpy as np
n = 100
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 十张扑克牌
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for j in range(n):
    np.random.shuffle(list)  # 洗牌
    i = list.index(10)
    a[i] = a[i]+1  # 记录每个人抽到10的次数
print(a)    # 输出每个人抽到10的总次数
frequency = np.array(a)/n
print(frequency)  # 输出每个人抽到10的频率

# 用整数1-10 来模拟实验的结果，在1-10十个整数中，假设整数10代表抽到大王，
# 将这十个数重新排序，整数10出现在哪个位置就代表该位置上的人抽到了大王
