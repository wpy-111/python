#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import datetime
import time
import os
import cv2
import config
from detectors import *
from widgets import Button
from camera import Camera
from driver import Driver, SLOW_DOWN_RATE
from cruiser import Cruiser
front_camera = Camera(config.front_cam, [640, 480])
side_camera = Camera(config.side_cam, [640, 480])
driver = Driver()
cruiser = Cruiser()
#程序开启运行开关
start_button = Button(1, "UP")
#程序关闭开关
stop_button = Button(1, "DOWN")

#确认"DOWN"按键是否按下，程序是否处于等待直行状态
def check_stop():
    if stop_button.clicked():
        video.release()
        driver.stop()
        side_camera.stop()
        os.system('sudo pkill python')
        return True
    return False
if __name__=='__main__':
    task_detector = TaskDetector()
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    video = cv2.VideoWriter('./video/video.avi', fourcc, 25, (160, 120))
    side_camera.start()
    #延时
    a = 0
    time.sleep(0.5)
    while True:
        if check_stop():
            break
        side_image = side_camera.read()
        res = task_detector.detect(side_image)
        print(res)
        xx = side_image.shape
        for item in res:
            left = item.relative_box[0] * xx[1]
            top = item.relative_box[1] * xx[0]
            right = item.relative_box[2] * xx[1]
            bottom = item.relative_box[3] * xx[0]
            start_point = (int(left), int(top))
            end_point = (int(right), int(bottom))
            color = (204, 0, 204)
            thickness = 2
            img = cv2.rectangle(side_image, start_point, end_point, color, thickness)
            filename = './video/' + str(a) + '.jpg'
            cv2.imwrite(filename,img)
            a += 1 