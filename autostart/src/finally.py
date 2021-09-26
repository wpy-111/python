#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import datetime
import time
import cv2
import os
# from .config import *
import config
from widgets import *
from camera import Camera
from driver import Driver, SLOW_DOWN_RATE
from detectors import SignDetector
from detectors import TaskDetector
from detectors import in_centered_in_image,is_target,is_trophies,is_soldier
from fixed_queue import FixedQueue
from obstacle import raiseflag, shot_target, capture_target, Lightwork,banyun,raise_finally
# 是否进行标志和目标物检测
camera_pwm = Servo(2)
enable_detection = True
# 前置摄像头
front_camera = Camera(config.front_cam, [640, 480])
# 侧边摄像头
side_camera = Camera(config.side_cam, [640, 480])
# 程序开启运行开关
start_button = Button(1, "UP")
stop_button = Button(1, "DOWN")
ultr_sensor = UltrasonicSensor(4)

servo1 = Servo(1)
# 车道巡航
driver = Driver()
# 地面标志检测
sign_detector = SignDetector()
# 侧边目标物检测
task_detector = TaskDetector()
STATE_IDLE = "idle"
STATE_CRUISE = "cruise"
STATE_SIGN_DETECTED = "sign_detected"
STATE_TASK = "task"
STATE_TASK_8 = "go_task8"
MISS_DURATION = 600
SLOW_DOWN_TIME = 3
TEMP_STOP_TIME = 5
handled_taskes = set("target")
handled_taskes.add("barracks")
handled_taskes.add('fenglangjuxu')
handled_taskes.add('soldier')


#
OBSTACLE = 0
# 存储离目标较近的目标序列
task_queue_ = FixedQueue()

# candidate队列用类存储远一点的目标
candicate_queue_ = FixedQueue()

# for mession
mession_queue = FixedQueue(class_num=5)

# 任务次序记录
taskorder = 0

# 存储视野中较近的检测到的目标
def task_queue():
    return task_queue_

# 相较task_queue队列，candidate队列用类存储远一点的目标
def candicate_queue():
    return candicate_queue_

# 筛选距离车体最近的标志和目标物
def select_queue(detect_res, blow_index, status):
    global task_queue_, candicate_queue_

    # no object detected
    if len(detect_res) == 0:
        task_queue_.append(0)
        candicate_queue_.append(0)
    count = 0
    for item in detect_res:
        label = item.index
        # 距离较远的框不插入？
        y_bar = 0.5
        if item.index == 2:  # 封狼居胥
            y_bar = 0.6
        elif item.index == 1:#宿营
            y_bar = 0.3
        elif item.index == 7:  # obstacle;
            y_bar = 0.7
        elif item.index == 5:#打标
            y_bar = 0.5
        elif item.index == 4:#soldier
            y_bar = 0.3
        if item.relative_box[3] > y_bar:
            if count == blow_index and status == 'cruise':
                task_queue_.append(1, label)
            else:
                candicate_queue_.append(1, label)
        count += 1

# 交换集合序列


def switch_queue():
    global task_queue_, candicate_queue_
    task_queue_, candicate_queue_ = candicate_queue_, task_queue_
# 打印已识别任务序列


def debug_queues():
    print("task queue is ")
    print(task_queue_.deque)
    print("candidate queue is")
    print(candicate_queue_.deque)
# 确认"DOWN"按键是否按下，程序是否处于等待直行状态


def check_stop(current_state):
    if current_state != STATE_IDLE and stop_button.clicked():
        return True
    return False
# 任务程序入口函数


def idle_handler(arg):
    while True:
        if start_button.clicked():
            time.sleep(0.3)
            return STATE_CRUISE, None
        # time.sleep(0.1);
        print("IDLE")
        driver.stop()
    return STATE_IDLE, None

# 规则中应该限制相邻两个标签的距离,中心距离大于3 / 4图像长度
# 摄像头视野frame图像中最多只包含两个目标物。


def cruise_handler(arg):
    # 任务完成标志（全局变量）
    # 任务标记量主要是为了误识别导致重复做任务
    global taskorder
    # counter =0
    flagnum = 0
    oldtime = time.time()
    # 设置小车巡航速度
    # driver.set_speed(driver.full_speed)
    if arg != None:
        start_time = time.time()
        cur_speed = driver.full_speed
        driver.set_speed(cur_speed * SLOW_DOWN_RATE)
    if taskorder == 2 or taskorder == 4:
        driver.set_speed(25)
    elif taskorder == 8:
        driver.set_speed(50)
    else:
        driver.set_speed(driver.full_speed)
    if taskorder == 5:
        driver.set_Kx(1.3)
    elif taskorder == 1 or taskorder == 8 or taskorder == 3:
        driver.set_Kx(0.95)
    else:
        driver.set_Kx(0.85)
    while True:
        if arg != None:
            cur_time = time.time()
            if cur_time - start_time > SLOW_DOWN_TIME:
                driver.set_speed(driver.full_speed)
            else:
                driver.set_speed(cur_speed * SLOW_DOWN_RATE)
        if check_stop(STATE_CRUISE):
            driver.stop()
            front_camera.stop()
            side_camera.stop()
            os.system('sudo pkill python')
            return STATE_IDLE, None
        front_image = front_camera.read()
        driver.go(front_image)
        if not enable_detection:
            continue
        if taskorder == 8:
            continue
        # 侦测车道上有无标志图标
        res, blow_index = sign_detector.detect(front_image, "cruise")
        # sign valid maybe task maybe just signal (bluesign, triangle, light)
        # 获取标志识别结果，获得所在列表的索引值
        flag, index = task_queue().roadsign_valid()
        if flag:
            flagnum += 1
            if flagnum < 2:
                continue
            else:
                if res and len(res) > 0:
                    select_queue(res, blow_index, "cruise")
                flagnum = 0
            sign_name = config.sign_list[index]
            print(sign_name)
            print(handled_taskes)
            if sign_name not in handled_taskes:
                if sign_name in ["barracks", "fenglangjuxu", "fortress", "soldier", "target"]:
                    return STATE_SIGN_DETECTED, sign_name
                else:
                    driver.set_speed(driver.full_speed)
                    print("cruise else mode {}".format(sign_name))
                    task_queue().clear()
                    continue
        if res and len(res) > 0:
            select_queue(res, blow_index, "cruise")

# 地面图标识别


def sign_detected_handler(arg):
    global taskorder
    if arg == "barracks" or arg == "fenglangjuxu" or arg == "soldier":
        handled_taskes.add(arg);
    cur_speed = driver.full_speed
    driver.set_speed(cur_speed * SLOW_DOWN_RATE)
    if taskorder ==2 or taskorder == 4:
        driver.set_speed(25)
    miss_mission = 0
    print(arg)
    # imgnum = 0
    barracksflag = True
    barracksnum = 0
    frontimagenum = 0
    disappearnum = 0
    print('============-------------===============------------============----------=========')
    while True:
        if check_stop(STATE_SIGN_DETECTED):
            driver.stop()
            front_camera.stop()
            side_camera.stop()
            os.system('sudo pkill python')
            return STATE_IDLE, None
        front_image = front_camera.read()
        driver.go(front_image)
        print("sign_detected")
        res_front, blow_index = sign_detector.detect(front_image, "cruise")
        print(res_front)
        if res_front and len(res_front) > 0:
            select_queue(res_front, blow_index, "cruise")
            frontimagenum += 1
        if taskorder == 2 or taskorder == 3:
            driver.set_speed(25)
            side_image = side_camera.read()
            res = task_detector.detect(side_image)

        elif frontimagenum > 1:
            if arg == "fenglangjuxu":
                driver.set_speed(cur_speed * 0.5)
            else:
                driver.set_speed(cur_speed * SLOW_DOWN_RATE)
            side_image = side_camera.read()
            res = task_detector.detect(side_image)
        else:
            driver.set_speed(cur_speed*0.8)
            continue

        if len(res) > 0:
            print(res)
            miss_mission = 0
            if res[0].name == "target":
                if taskorder == 1 or taskorder == 2 or taskorder == 3:
                    num_target = is_target(res)
                    if num_target == 1:
                        print("stepping into target")
                        task_queue().clear()
                        driver.stop()
                        time.sleep(0.3)
                        frontimagenum = 0
                        print("+++++++++++++++++++start task!res=", res)
                        return STATE_TASK, res
                    elif num_target == -1:
                        # driver.set_speed(-8
                        driver.driver_run(-8,-8)
                        time.sleep(0.6)
                    else:
                        driver.set_speed(8)

            elif res[0].name =="trophies" and taskorder == 5:
                num_trophies = is_trophies(res)
                if num_trophies == 1:
                    print("stepping into target")
                    task_queue().clear()
                    driver.stop()
                    time.sleep(0.1)
                    frontimagenum = 0
                    print("+++++++++++++++++++start task!res=", res)
                    return STATE_TASK, res
                elif num_trophies == -1:
                    driver.set_speed(-8)
                    time.sleep(0.2)
                else:
                    driver.set_speed(8)

            elif res[0].name == "daijun" or res[0].name == "dunhuang" or res[0].name == "dingxiangjun":
                if taskorder == 0 or taskorder == 1 or taskorder == 7:
                    if in_centered_in_image(res):
                        print("stepping into task")
                        task_queue().clear()
                        driver.stop()
                        time.sleep(0.3)
                        # 后续右侧任务
                        # return STATE_CRUISE, None
                        frontimagenum = 0
                        print("+++++++++++++++++++start task!res=", res)
                        return STATE_TASK, res
            elif res[0].name == "soldier" and taskorder == 6:
                num_soldier = is_soldier(res)
                if num_soldier == 1:
                    print("stepping into target")
                    task_queue().clear()
                    driver.stop()
                    time.sleep(0.3)
                    frontimagenum = 0
                    print("+++++++++++++++++++start task!res=", res)
                    return STATE_TASK, res
                elif num_soldier == -1:
                    driver.set_speed(-8)
                    time.sleep(0.2)
                else:
                    driver.set_speed(8)

        else:
            miss_mission += 1
        if miss_mission > 30:
            print("detected miss, stepping into cruise")
            task_queue().clear()
            switch_queue()
            driver.set_speed(cur_speed)
            return STATE_CRUISE, None

# 做任务


def task_handler(res):
    global taskorder
    print("task")
    print("res=", res)
    cur_speed = driver.full_speed
    driver.set_speed(cur_speed)
    if res == "barracks":
        driver.stop()
        time.sleep(0.2)
        driver.driver_run(30, 30)
        time.sleep(1.65)
        driver.driver_run(-8, -30)
        time.sleep(1.2)
        driver.driver_run(-30, -30)
        time.sleep(0.7)
        driver.driver_run(-30, -8)
        time.sleep(1.1)
        driver.stop()
        for i in range(0, 4):
            Lightwork(2, "red")
            time.sleep(0.02)
            Lightwork(2, "off")
        driver.driver_run(30, 8)
        time.sleep(1)
        driver.driver_run(30, 30)
        time.sleep(0.75)
        driver.driver_run(8, 30)
        time.sleep(1)
        driver.stop()
        taskorder = 5
    else:
        name = res[0].name
        if name == "soldier":
            motor = 3
            driver.stop()
            time.sleep(0.2)
            banyun(motor)
            taskorder = 7
        elif name == "daijun":
            if taskorder == 0:
                driver.driver_run(-20, -20)
                time.sleep(0.7)
                driver.stop()
                taskorder = 1
                raiseflag(4, 3)
            elif taskorder == 1:
                driver.driver_run(20, 20)
                time.sleep(0.6)
                driver.stop()
                taskorder = 7
                raiseflag(4, 3)
            else:
                driver.driver_run(-20, -20)
                time.sleep(0.7)
                driver.stop()
                taskorder = 8
                raise_finally(4, 3)
        elif name == "dingxiangjun":
            if taskorder == 0:
                driver.driver_run(-20, -20)
                time.sleep(0.7)
                driver.stop()
                taskorder = 1
                raiseflag(4, 3)
            elif taskorder == 1:
                driver.driver_run(20, 20)
                time.sleep(0.6)
                driver.stop()
                taskorder = 7
                raiseflag(4, 3)
            else:
                driver.driver_run(-20, -20)
                time.sleep(0.7)
                driver.stop()
                taskorder = 8
                raise_finally(4, 3)

        elif name == "dunhuang":
            if taskorder == 0:
                driver.driver_run(-20, -20)
                time.sleep(0.7)
                driver.stop()
                taskorder = 1
                raiseflag(4, 3)
            elif taskorder == 1:
                driver.driver_run(20, 20)
                time.sleep(0.6)
                driver.stop()
                taskorder = 7
                raiseflag(4, 3)
            else:
                driver.driver_run(-20, -20)
                time.sleep(0.7)
                driver.stop()
                taskorder = 8
                raise_finally(4, 3)

        elif name == "target":

            driver.stop()
            time.sleep(0.3)
            shot_target(2)
            taskorder += 1

        elif name == "trophies":
            driver.stop()
            time.sleep(0.3)
            capture_target(1,3)
            time.sleep(0.5)
            taskorder = 6
        else:
            print("Error!#####################")

    # 右侧任务
    if taskorder == 1 or taskorder == 2 or taskorder == 6 or taskorder == 3:
        camera_pwm.servocontrol(-113,70)
        time.sleep(0.1)
    # 后续左侧任务
    else:
        camera_pwm.servocontrol(50,70)
        time.sleep(0.1)
    switch_queue()

    print("taskorder:",taskorder)
    return STATE_CRUISE, None


def go_task_8(arg):
    global taskorder
    print("go_task_8")
    cur_speed = driver.full_speed
    driver.set_speed(cur_speed)
    task8_start = time.time()
    while True:
        front_image = front_camera.read()
        driver.go(front_image)
        if time.time()-task8_start < 4:
            driver.set_Kx(0.7)
            continue
        elif time.time()-task8_start < 5:
            driver.set_Kx(0.8)
        else:
            driver.set_Kx(0.9)
        um = ultr_sensor.read()
        # print("*8888888")
        if um != None and um < 20:
            driver.stop()
            return STATE_TASK, "dingxiangjun"


state_map = {
    STATE_IDLE: idle_handler,
    STATE_CRUISE: cruise_handler,
    STATE_SIGN_DETECTED: sign_detected_handler,
    STATE_TASK: task_handler,
    STATE_TASK_8: go_task_8,
}


def main():
    camera_pwm.servocontrol(50,70)
    servo1.servocontrol(0, 50)
    time.sleep(0.5)
    current_state = STATE_IDLE
    arg = None
    front_camera.start()
    side_camera.start()
    Lightwork(2, "red")
    time.sleep(0.5)
    Lightwork(2, "green")
    time.sleep(0.5)
    Lightwork(2, "off")
    try:
        while (True):
            new_state, arg = state_map[current_state](arg)
            current_state = new_state
        driver.stop()
        front_camera.stop()
        side_camera.stop()
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
        driver.stop()
        Lightwork(2, "off")
        Lightwork(4, "off")


if __name__ == "__main__":
    main()
