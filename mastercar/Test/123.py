import cv2
import time
cap = cv2.VideoCapture('video.avi')
time1 = time.time()
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('frame', gray)
    key = cv2.waitKey(100)
    time2 = time.time()
    print(time2-time1)
    if key == ord('q'):
        print(key)
        break
cap.release()
cv2.destroyAllWindows()
