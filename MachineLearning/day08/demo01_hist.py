"""
    直方图均衡化
"""
import cv2 as cv
original = cv.imread('lily.jpg')
cv.imshow('original',original)
#提取灰度图像
gray = cv.cvtColor(original,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#直方图均衡化
e_gray = cv.equalizeHist(gray)
cv.imshow('e_gray',e_gray)
#彩色图像直方图j均衡化   yuv 亮度，色度，饱和度
yuv = cv.cvtColor(original,cv.COLOR_BGR2YUV)
yuv[:,:,0] = cv.equalizeHist(yuv[:,:,0])
color = cv.cvtColor(yuv,cv.COLOR_YUV2BGR)
cv.imshow('color',color)
cv.waitKey()