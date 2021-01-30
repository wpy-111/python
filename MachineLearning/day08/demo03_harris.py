"""
    角点检测
"""
import cv2 as cv
original = cv.imread('lily.jpg')
cv.imshow('original',original)
gray = cv.cvtColor(original,cv.COLOR_BGR2GRAY)
corner = cv.cornerHarris(gray,7,5,0.04)
print(corner.shape)
cv.imshow('corner',corner)
original[corner>0.001] = [0,0,255]
cv.imshow('original',original)
cv.waitKey()