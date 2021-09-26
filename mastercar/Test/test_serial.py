import cv2
import numpy as np


def canny():
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    #高斯滤波
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
	#边缘检测
    canny_img = cv2.Canny(blur, 50, 150)
    return canny_img


def region_of_interest(r_image):
    h = r_image.shape[0]
    w = r_image.shape[1]
	# 这个区域不稳定，需要根据图片更换
    poly = np.array([
        [(100, h), (500, h), (290, 180), (250, 180)]
    ])
    mask = np.zeros_like(r_image)
    # 绘制掩膜图像
    cv2.fillPoly(mask, poly, 255)
    # 获得ROI区域
    masked_image = cv2.bitwise_and(r_image, mask)
    return masked_image


if __name__ == '__main__':
    image = cv2.imread('7.png')
    lane_image = np.copy(image)
    canny = canny()
    # cropped_image = region_of_interest(canny)
    cv2.imshow("result", canny)
    cv2.waitKey(0)
