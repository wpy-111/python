#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import datetime
import time
import cv2
import os
import config
from widgets import Button
from detectors import *
from cruiser import Cruiser
from cart import Cart
from driver import Driver
import threading
front_camera = Camera(config.front_cam, [640, 480])
driver = Driver()
cruiser = Cruiser()

#程序开启运行开关
start_button = Button(1, "UP")
#程序关闭开关
stop_button = Button(1, "DOWN")

#确认"DOWN"按键是否按下，程序是否处于等待直行状态
def check_stop():
    if stop_button.clicked():
        return True
    return False
def start():
    while True:
        front_image = front_camera.read()
        angle = cruiser.cruise(front_image)
        driver.go(front_image)
        results, blow_center_index = sign_detector.detect(front_image)
        print("res:",results,'blow_center_index:',blow_center_index)
        if blow_center_index == -1:
            frame = cv2.putText(front_image,str(angle), (40, 50), font, 2, color, 2)
        else:
            frame = cv2.putText(front_image, str(angle), (50, 50), font, 2, color, 2)
            frame = draw_res(frame,results)
        videoWriter.write(frame)
def end():
    while True:
        if check_stop():
            driver.stop()
            videoWriter.release()
            front_camera.stop()
            os.system('sudo pkill python')

if __name__=='__main__':
    front_camera.start()
    #基准速度
    driver.set_speed(45)
    #转弯系数
    driver.cart.Kx=0.9
    #延时
    time.sleep(0.5)
    sign_detector = SignDetector()
    color = (0,255,0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    videoWriter = cv2.VideoWriter('./video/video.avi', fourcc, 15, (640, 480))
    while True:
        if start_button.clicked():
            time.sleep(0.3)
            break
        print("Wait for start!")
    t1 = threading.Thread(target=start)
    t2 = threading.Thread(target=end)
    t1.start()
    t2.start()



