"""
    边缘检测
"""
import cv2 as cv
#直接获取灰度图
original = cv.imread('lily.jpg',0)
cv.imshow('original',original)
result = cv.Canny(original,100,100)
cv.imshow('result',result)
cv.waitKey()




