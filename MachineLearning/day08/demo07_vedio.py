"""
    视频捕获
"""
import cv2 as cv
import time
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]
    cv.imshow('frame',frame)
    #27是esc按esc退出
    if cv.waitKey(100)==27:
        break
vc.release()
cv.destroyAllWindows()