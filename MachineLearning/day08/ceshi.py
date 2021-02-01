import cv2 as cv
original = cv.imread('0.png')
print(original.shape)
img = cv.cvtColor(original,cv.COLOR_BGR2GRAY)
cv.imshow('img',img)
img2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3,1)
cv.imshow('img2',img2)
cv.waitKey()