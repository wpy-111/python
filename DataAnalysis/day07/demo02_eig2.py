"""
    图片特征提取
"""
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp

img = sm.imread('./lily.jpg',True)
#转矩阵
img = np.mat(img)
#提取图像特征
eigvals,eigvecs = np.linalg.eig(img)
mp.imshow(img,cmap='gray')
mp.show()


