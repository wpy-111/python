"""
    奇异值影响
"""
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp

img = sm.imread('./lily.jpg',True)
#转矩阵
img = np.mat(img)
#提取图像奇异值
U,S,V = np.linalg.svd(img)
S[50:] = 0
#逆推矩阵
img2= U*np.diag(S)*V

mp.subplot(121)
mp.imshow(img,cmap='gray')
mp.subplot(122)
mp.imshow(img2.real,cmap='gray')

mp.show()