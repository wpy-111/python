"""
  3d曲面图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
n = 500
x,y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
#通过每个xy的值算出z的值
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

mp.figure('3D PlotSurface',facecolor='lightgrey')
mp.title('3D SurFace',fontsize=16)
ax3d = mp.gca(projection='3d')#三维坐标系
ax3d.plot_surface(x,y,z,cmap='jet',rstride=30,cstride=30)
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
mp.grid(linestyle=':')
mp.tight_layout()
mp.show()





