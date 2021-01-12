"""
  三维三点图
"""
import numpy as np
import matplotlib.pyplot as mp
import mpl_toolkits.mplot3d as axes3d
n = 200
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
z = np.random.normal(0,1,n)

mp.figure('3D Scatter',facecolor='lightgrey')
mp.title('3D Scatter',fontsize=16)
axes = mp.gca(projection='3d')
d = x**2+y**2+z**2
axes.scatter(x,y,z,s=80,alpha=0.8,marker='o',c=d,cmap='jet')
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_zlabel('Z')

mp.tight_layout()
mp.show()
