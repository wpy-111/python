"""
demo02_plot.py  sinx
"""
import numpy as np
import matplotlib.pyplot as mp
#从-Π到Π拆1000个点
x = np.linspace(-np.pi,np.pi,1000)

sinx = np.sin(x)
cosx = np.cos(x)

#修改X轴的刻度文本
vals = [-np.pi,-np.pi/2,0,np.pi/2,np.pi]
texts = [r'$-\pi$',r'$-\frac{\pi}{2}$',0,r'$\frac{\pi}{2}$',r'$\pi$']
mp.xticks(vals,texts)
#更改坐标轴
axis = mp.gca()
axis.spines['top'].set_color('none')
axis.spines['right'].set_color('none')
axis.spines['left'].set_position(('data',0))
axis.spines['bottom'].set_position(('data',0))

mp.plot(x,sinx,linestyle = '-.',linewidth = '2',color = 'dodgerblue',alpha = 0.8,label=r'$y=sin(x)$')
mp.plot(x,cosx,linestyle = '--',linewidth = '3',color = 'orangered',alpha = 0.5,label=r'$y=\frac{1}{2}cos(x)$')

xs = [np.pi/2,np.pi/2]
ys = [1,0]
#绘制特殊点
mp.scatter(xs,ys,s=80,edgecolors='red',facecolor='green',marker='D',label='Points',zorder=3)

mp.title("square")  # 图标题
#设置备注
mp.annotate(r'$[\frac{\pi}{2},1]$',xycoords='data',xy=(np.pi/2,1),textcoords='offset points',xytext=(30,20),fontsize=14,
            arrowprops=dict(arrowstyle='->',connectionstyle='angle3'))
mp.annotate(r'$[\frac{\pi}{2},0]$',xycoords='data',xy=(np.pi/2,0),textcoords='offset points',xytext=(-50,-30),
            fontsize=15,arrowprops=dict(arrowstyle='->',connectionstyle='angle3'))
#legend图例
mp.legend()
mp.show()




