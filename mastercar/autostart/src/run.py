#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import datetime
import time
import os
import cv2
import config
from widgets import Button
from threading import Thread
from camera import Camera
from cruiser import Cruiser
from driver import Driver
from detectors import TaskDetector
from serial_port import serial_connection
serial = serial_connection
a = 0
front_camera = Camera(config.front_cam, [640, 480])
#side_camera = Camera(config.side_cam, [640, 480])

driver = Driver()
cruiser = Cruiser()
task = TaskDetector()
#程序开启运行开关
start_button = Button(1, "UP")
#程序关闭开关
stop_button = Button(1, "DOWN")

#确认"DOWN"按键是否按下，程序是否处于等待直行状态
def check_stop():
    if stop_button.clicked():
        return True
    return False

def do_task():
    while True:
        global a
        front_image = front_camera.read()
        filename1 = './front_image/' + str(a) + '.jpg'
        cv2.imwrite(filename1,front_image)
        result = driver.go(front_image)
        if result is None:
            continue
        # else:
        #     side_image = side_camera.read()
        #     filename = './side_image/'+str(a)+'.jpg'
        #     cv2.imwrite(filename,side_image)
        #     for item in result:
        #         if item[1] < 0.5:
        #             continue
        #         print("name:", item[0], "   ", "score:", item[1])
        #         result = task.detect(side_image)
        #         if result is None:
        #             continue
        #         print(result)
        a += 1
def stop_task():
    while True:
        if check_stop():
            driver.stop()
            print("End of program!")
            front_camera.stop()
            os.system('sudo pkill python')

if __name__=='__main__':
    front_camera.start()
    side_camera.start()
    #基准速度
    driver.set_speed(25)
    #转弯系数
    driver.cart.Kx=0.9
    #延时
    time.sleep(1)
    while True:
        if start_button.clicked():
            time.sleep(0.3)
            break
        print("Wait for start!")
    p1 = Thread(target=do_task)
    p2 = Thread(target=stop_task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


