import os
import cv2 as cv
list = os.listdir('../day01')
print(list)

Path1 = 'home'
Path2 = 'develop'
Path3 = 'code'

Path10 = Path1 + Path2 + Path3
Path20 = os.path.join(Path1, Path2, Path3)
print('Path10 = ', Path10)
print('Path20 = ', Path20)
img = cv.imread('../day01\4000.png')
cv.imshow('img',img)
cv.waitKey()

