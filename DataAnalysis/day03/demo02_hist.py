"""
     直方图
"""
import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm

img = sm.imread('./lily.jpg')
x = img.ravel()
mp.figure("Image Hist",facecolor='lightgrey')
#绘制直方图
#mp.hist(
#     x, 					# 值列表
#     bins, 				# 直方柱数量
#     color, 				# 颜色
#     edgecolor, 			# 边缘颜色
#     normed=True, 		# 是否以密度方式显示
# )
mp.hist(x,bins=10,color='dodgerblue',edgecolor='white')
mp.xticks(np.linspace(0,255,11))
mp.show()
