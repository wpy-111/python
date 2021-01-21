"""
    线性回归  梯度下降自己会去找最小的      x = x-学习率*导函数（偏导数）
"""
import numpy as np
import matplotlib.pyplot as mp
train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
lrate = 0.01
k_list,b_list=[1],[1]
losses = []
times = 1000
epoches = []	# 记录每次梯度下降的索引
for i in range(times):
    loss = ((k_list[-1]*train_x+b_list[-1]-train_y) **2).sum()/2
    losses.append(loss)
    print("loss:{},k:{},b={}".format(losses[-1],k_list[-1],b_list[-1]))
    # 根据自己推导的偏导公式计算出k的偏导数
    k0 =(train_x*(b_list[-1]+k_list[-1]*train_x-train_y)).sum()
    #根据自己推导的偏导公式计算出b的偏导数
    b0 = (b_list[-1]+k_list[-1]*train_x-train_y).sum()
    #跟新参数
    k = k_list[-1]-lrate*k0
    b = b_list[-1]-lrate*b0
    k_list.append(k)
    b_list.append(b)
    epoches.append(i+1)
y = train_x*k_list[-1] + b_list[-1]
mp.figure("Line",facecolor='lightgrey')
mp.title('Line',fontsize=16)
mp.grid(linestyle=':')
mp.xlabel('train_x')
mp.ylabel('train_y')
mp.scatter(train_x,train_y,s=80,marker='o',color='dodgerblue',label='genuine')
mp.plot(train_x,y,linestyle='-',linewidth=2,color='orangered',label='pred')
mp.legend()
k_list = k_list[:-1]
b_list = b_list[:-1]
mp.figure('参数',facecolor='lightgrey')
mp.title('参数',fontsize=16)
mp.subplot(311)
mp.grid()
mp.plot(epoches,k_list,color='dodgerblue',label='k')
mp.ylabel('k',fontsize=14)
mp.tight_layout()
mp.legend()
mp.subplot(312)
mp.grid()
mp.plot(epoches,b_list,color='dodgerblue',label='b')
mp.ylabel('b',fontsize=14)
mp.tight_layout()
mp.legend()
mp.subplot(313)
mp.grid()
mp.plot(epoches,k_list,color='dodgerblue',label='loss')
mp.ylabel('loss',fontsize=14)
mp.tight_layout()
mp.legend()
import mpl_toolkits.mplot3d as axes3d

grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))

grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
    grid_loss += ((grid_w0 + x*grid_w1 - y) ** 2) / 2

mp.figure('Loss Function')
ax = mp.gca(projection='3d')
mp.title('Loss Function', fontsize=20)
ax.set_xlabel('w0', fontsize=14)
ax.set_ylabel('w1', fontsize=14)
ax.set_zlabel('loss', fontsize=14)
ax.plot_surface(grid_w0, grid_w1, grid_loss, rstride=10, cstride=10, cmap='jet')
#o-是用红色标记出点的位置  bo是蓝色
ax.plot(b_list, k_list, losses,'o-', c='red',linewidth=1, label='BGD')
mp.legend()
mp.show()

