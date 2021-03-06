"""
    人工分类
"""
import numpy as np
import matplotlib.pyplot as mp
x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
#生成网格坐标点
n = 500
l,r = x[:,0].min()- 1,x[:,0].max()+1
b,t = x[:,1].min()-1,x[:,1].max()+1
grid_x,grid_y = np.meshgrid(np.linspace(l,r,n),np.linspace(b,t,n))
grid_z = np.zeros_like(grid_x)
grid_z[grid_x<grid_y] = 1
#绘制样点的散点图
mp.figure('Clasification',facecolor='lightgrey')
mp.title('Clasification',fontsize=16)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')#画好背景才能描点
mp.scatter(x[:,0],x[:,1],c=y,cmap='brg_r',s=80,label='Samples')
mp.legend()
mp.tight_layout()
mp.show()
# ax3d = mp.gcf(projection='3d')



