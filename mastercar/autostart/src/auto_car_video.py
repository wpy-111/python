#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import time
import cv2
import config
from widgets import Button
from camera import Camera
from driver import Driver, SLOW_DOWN_RATE
from cruiser import Cruiser
from serial_port import serial_connection
from threading import Thread

serial = serial_connection
front_camera = Camera(config.front_cam, [640, 480])
side_camera = Camera(config.side_cam, [640, 480])

driver = Driver()
cruiser = Cruiser()
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
videoWriter = cv2.VideoWriter('./video/video.avi', fourcc, 15, (640,480))

#程序开启运行开关
start_button = Button(1, "UP")
#程序关闭开关
stop_button = Button(1, "DOWN")

#确认"DOWN"按键是否按下，程序是否处于等待直行状态
def check_stop():
    if stop_button.clicked():
        return True
    return False

def do_tast():
    a = 0
    while True:
        start = time.time()
        front_image = front_camera.read()
        img = driver.go_video(front_image,a)
        if img is None:
            continue
        videoWriter.write(img)
        a += 1
        end = time.time()
        print("执行时间：",end-start)


def stop_task():
    while True:
        if check_stop():
            driver.stop()
            videoWriter.release()
            print("End of program!")
            front_camera.stop()
            os.system('sudo pkill python')

if __name__=='__main__':
    front_camera.start()

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
    p1 = Thread(target=do_tast)
    p2 = Thread(target=stop_task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()



