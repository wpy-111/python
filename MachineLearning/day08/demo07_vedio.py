"""
    视频捕获
"""
import cv2 as cv
vc = cv.VideoCapture(1)
while True:
    frame = vc.read()[1]
    cv.imshow('frame',frame)
    #27是esc按esc退出
    if cv.waitKey(20)==27:
        break
vc.release()
cv.destroyAllWindows()