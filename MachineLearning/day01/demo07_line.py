"""
    线性回归  梯度下降自己会去找最小的      x = x-学习率*导函数（偏导数）
"""
import numpy as np
import matplotlib.pyplot as mp
train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
lrate = 0.01
k,b=1,1
loss = ((k*train_x+b-train_y) **2).sum()/2
for i in range(10000):
    # 根据自己推导的偏导公式计算出k的偏导数
    k0 =(train_x*(b+k*train_x-train_y)).sum()
    #根据自己推导的偏导公式计算出b的偏导数
    b0 = (b+k*train_x-train_y).sum()
    #跟新参数
    k = k-lrate*k0
    b = b-lrate*b0

y = train_x*k + b
mp.figure("Line",facecolor='lightgrey')
mp.title('Line',fontsize=16)
mp.grid(linestyle=':')
mp.xlabel('train_x')
mp.ylabel('train_y')
mp.scatter(train_x,train_y,s=80,marker='o',color='dodgerblue',label='genuine')
mp.plot(train_x,y,linestyle='-',linewidth=2,color='orangered',label='pred')
mp.legend()
mp.show()

