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
#绘制样点的散点图
from mpl_toolkits.mplot3d import axes3d
mp.figure('Clasification',facecolor='lightgrey')
mp.title('Clasification',fontsize=16)
mp.grid(':')
mp.scatter(x[:,0],x[:,1],c=y,cmap='jet',s=80,label='Samples')
mp.pcolormesh(x[:,0],x[:,1],c=y,cmap='jet')
mp.legend()
mp.tight_layout()
mp.show()
# ax3d = mp.gcf(projection='3d')



