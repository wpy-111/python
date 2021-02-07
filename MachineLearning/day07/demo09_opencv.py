"""
    opencv基础
"""
import numpy as np
import cv2 as cv
original = cv.imread('lily.jpg')
print(original[0,0])
cv.imshow('original',original)
size = cv.resize(original,(300,200))
cv.imshow('size',size)
# #图片的本质是三维数组
# red = np.ones_like(original)
# red[:,:,2] = original[:,:,2]
# cv.imshow('red',red)
# #彩色图片裁剪
# cropped = original[0:200,0:300,:]
# cv.imshow('cropped',cropped)
# #图形伸缩  第二个参数是反的 （列，宽）
# scale1 = cv.resize(original,(300,200))
# cv.imshow('scale1',scale1)
# #fx设置比例
# scale2 = cv.resize(original,None,fx=0.5,fy=0.5)
# cv.imshow('scale2',scale2)
# #图像保存
# cv.imwrite('red.jpg',red)
# cv.imwrite('red.png',red)

cv.waitKey()
