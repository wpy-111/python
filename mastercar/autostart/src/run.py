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
        driver.go(front_image)
def end():
    while True:
        if check_stop():
            driver.stop()
            front_camera.stop()
            os.system('sudo pkill python')

if __name__=='__main__':
    front_camera.start()
    #基准速度
    driver.set_speed(45)
    #转弯系数
    driver.cart.Kx=0.9
    #延时
    while True:
        if start_button.clicked():
            time.sleep(0.3)
            break
        print("Wait for start!")
    t1 = threading.Thread(target=start)
    t2 = threading.Thread(target=end)
    t1.start()
    t2.start()



