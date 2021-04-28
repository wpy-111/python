import cv2
import numpy as np
from PIL import Image
frame = cv2.imread('7.png')
frame = cv2.resize(frame,(300,300))
h, w = 300, 300
x1 = int(0.1 * w)
x2 = int(0.2 * w)
y1 = int(0.3 * w)
y2 = int(0.4 * w)
print(x1, '1111111111111')
print(y2, '====0')

colors = (0, 0, 255)
cv2.rectangle(frame, (x1, y1), (x2, y2), colors, 5)
cv2.putText(frame, "label", (50, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
# filename = './images/' + str(a) + '.jpg'
# cv2.imwrite(filename, frame)
cv2.imwrite('0.jpg',frame)
cv2.imshow('111',frame)
cv2.waitKey()