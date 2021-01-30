"""
    哈尔级联定位器
"""
import cv2 as cv
# 哈尔级联人脸定位器
fd = cv.CascadeClassifier('..\\data\\face.xml')
ed = cv.CascadeClassifier('..\\data\\eye.xml')
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]
    faces = fd.detectMultiScale(frame, 1.3, 5)
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        cv.ellipse(frame, (l + a, t + b), (a, b), 0, 0, 360, (255, 0, 255), 2)
        face = frame[t:t + h, l:l + w]
        eyes = ed.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in eyes:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 0), 2)
        # noses = nd.detectMultiScale(face, 1.3, 5)
        # for l, t, w, h in noses:
        #     a, b = int(w / 2), int(h / 2)
        #     cv.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 255), 2)
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:
        break
vc.release()