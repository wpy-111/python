import os
import sys
import time
from cruiser import Cruiser
from cart import Cart
from detectors import SignDetector
from model_validator import draw_boxes
from model_validator import draw_line
number = 0
class Driver:
    def __init__(self):
        self.max_speed=40
        self.full_speed = 40
        self.cart = Cart()
        self.cart.velocity=self.full_speed
        self.cruiser = Cruiser()
        self.detection = SignDetector()

    def stop(self):
        self.cart.stop()

    def go_video(self, frame,a):
        img = self.car_line(frame,a)
        img = self.image_detection(img,a,frame)
        return img

    def go(self,frame):
        angle = self.cruiser.cruise(frame)
        results = self.detection.detect(frame)
        self.cart.steer(angle)
        return results

    def speed(self):
        return self.cart.velocity

    def set_speed(self, speed):
        # self.full_speed=speed
        self.cart.velocity=speed

    def set_Kx(self, Kx):
        self.cart.Kx=Kx

    def get_min_speed(self):
        return self.cart.min_speed

    def change_posture(self, basespeed):
        # basespeed=15
        l_speed = basespeed
        r_speed = basespeed * 0.4
        self.cart.move([l_speed, r_speed, l_speed, r_speed])
        time.sleep(1)
        l_speed = basespeed * 0.4
        r_speed = basespeed
        self.cart.move([l_speed, r_speed, l_speed, r_speed])
        time.sleep(1)
        self.cart.stop()

    def car_line(self,frame,a):
        angle = self.cruiser.cruise(frame)
        img = draw_line(frame,angle,a)
        self.cart.steer(angle)
        return img

    def image_detection(self,frame,a,img):
        results = self.detection.detect(img)
        frame = draw_boxes(frame,results,a)
        return frame

    def change_posture_cm(self, distance):
        basespeed = 15
        speed_ratio = 0.4
        drivetime = distance * 0.9
        if distance < 2:
            speed_ratio = 0.2
            drivetime = distance * 0.95
        elif distance < 4:
            speed_ratio = 0.15
            drivetime = distance * 0.75
        else:
            speed_ratio = -0.05
            drivetime = distance * 0.5
        l_speed = basespeed
        r_speed = basespeed * speed_ratio
        self.cart.move([l_speed, r_speed, l_speed, r_speed])
        time.sleep(drivetime)
        l_speed = basespeed * speed_ratio
        r_speed = basespeed
        self.cart.move([l_speed, r_speed, l_speed, r_speed])
        time.sleep(drivetime-0.5)
        self.cart.stop()
    def driver_run(self,left,right):
        self.cart.move([left,right,left,right])

# d = Driver();
SLOW_DOWN_RATE = 0.6
if __name__ == '__main__':
    d = Driver()
    print("hoinonogei")
    # d.change_posture(20)
    d.change_posture_cm(5)
