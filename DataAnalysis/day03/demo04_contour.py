"""
  等高线图
"""
import numpy as np
import matplotlib.pyplot as mp

n = 500
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
#通过每个xy的值算出z的值
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
#画图
mp.figure("Contour",facecolor='lightgrey')
mp.title('Contour',fontsize=16)
mp.grid(linestyle=':')
cntr = mp.contour(x,y,z,8,color='black',linewidths=0.5)
## 为等高线图添加高度标签
mp.clabel(cntr,inline_spacing=1,fmt='%.1f',fontsize=10)
mp.contourf(x,y,z,cmap='jet')
mp.show()










