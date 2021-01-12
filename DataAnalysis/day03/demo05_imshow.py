"""
    图形化二维数组
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm
img = sm.imread('./lily.jpg',True)
print(img.shape)
mp.figure('Image',facecolor='lightgrey')
#图形化显示二维数组imshow（）
mp.imshow(img,cmap='jet')
mp.show()