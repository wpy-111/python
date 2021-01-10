"""
    matplotlib
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.array([1,2,3,4,5])
y = np.array([28,7,56,88,102])

mp.plot(x,y)

#绘制水平线和垂直线
mp.hlines(30,2,4)
mp.vlines(3,10,70)
mp.show()


