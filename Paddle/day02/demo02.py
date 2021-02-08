import cv2 as cv
import os

dir = '../day01'
list = os.listdir(dir)
for i in list:
    if  i == '4000.png':
        file = os.path.join(dir,i)
        print(file)
        img =cv.imread(file)
        cv.imshow('img',img)
        cv.waitKey()
        break
