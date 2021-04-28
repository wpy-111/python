import cv2
import numpy as np
from PIL import Image
img = cv2.imread('7.png')
lower_hsv = np.array([20, 75, 160])
upper_hsv = np.array([40, 255, 255])
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
mask = cv2.resize(mask, (128, 128))
img = Image.fromarray(mask)
img = np.array(img).astype(np.float32)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.imshow('img',img)
img = img / 255.0
img = np.expand_dims(img, axis=0)
cv2.waitKey()
