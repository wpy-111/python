"""
   动画操作
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
#随机生成一百个点
n = 100
balls = np.zeros(n,dtype=[('size','f8',1),
                  ('position','f8',2),
                  ('color','f8',4),
                  ('growth','f8',1)])
#数据初始化  均匀分布出现概率一样
balls['size'] = np.random.uniform(40,70,n)
balls['position'] = np.random.uniform(0,1,(n,2))
balls['color'] = np.random.uniform(0,1,(n,4))
balls['growth'] = np.random.uniform(10,20,n)
mp.figure('Animation',facecolor='lightgrey')
mp.title('Animation',fontsize=16)
sc = mp.scatter(balls['position'][:,0],balls['position'][:,1],s=balls['size'],color=balls['color'])
#定义动画，执行动画
def update(number):
    #调处一个点，重置这个点的大小，位置
    ind = number % n
    balls[ind]['size'] = np.random.uniform(40,70,1)
    balls[ind]['position'] = np.random.uniform(0,1,(1,2))
    balls['size'] += balls['growth']
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])
anim = ma.FuncAnimation(mp.gcf(),update,interval=30)
mp.show()

