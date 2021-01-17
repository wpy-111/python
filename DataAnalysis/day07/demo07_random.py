"""
    随机数 二项分布
"""
# import numpy as np
# r = np.random.binomial(10,0.3,100)
# print(r)
import numpy as np
import matplotlib.pyplot as mp

# binomial: 从二项分布中抽取样本
# n:尝试次数  p:概率
r = np.random.binomial(10, 0.3, 200000)
# print(r)
total = 0
probs = []
for i in range(11):
    n = sum(r == i) / 200000
    print("i:", n)
    probs.append(n)
    total += n
print(total)

# 可视化
x = np.arange(0, 11)  # 产生均匀数组，长度等同于apples

mp.bar(x,  # 横轴数据
       probs,  # 纵轴数据
       0.4,  # 柱体宽度
       color='dodgerblue',
       label='probs')

mp.legend()
mp.show()