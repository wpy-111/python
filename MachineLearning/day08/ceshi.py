import cv2 as cv
original = cv.imread('0.png')
print(original.shape)
yuv = cv.cvtColor(original,cv.COLOR_BGR2YUV)
yuv[:,:,0] = cv.equalizeHist(yuv[:,:,0])
color = cv.cvtColor(yuv,cv.COLOR_YUV2BGR)
cv.imshow('color',color)
cv.waitKey()