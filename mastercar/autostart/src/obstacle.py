from widgets import Servo, Servo_pwm,Motor_rotate, Magneto_sensor,UltrasonicSensor,Light,Buzzer
from widgets import *
import time
import cart

def raiseflag(motor_port,magsensor_port):
    print("raiseflag start!")
    setmotor1 = Motor_rotate(motor_port)
    magsensor=Magneto_sensor(magsensor_port)
    setmotor1.motor_rotate(-20)
    # time.sleep(0.1)
    try:
        while True:
            if magsensor.read()!=None:
                ma=magsensor.read()
            else:
                ma=0
            print("ma=",ma)
            if ma>96 and ma != None:
                time.sleep(0.35)
                setmotor1.motor_rotate(0)
                time.sleep(0.1)
                break
    except Exception as e:
        print(e)
        while True:
            if magsensor.read() != None:
                ma = magsensor.read()
            else:
                ma = 0
            print("ma=", ma)
            if ma > 95 and ma != None:
                time.sleep(0.35)
                setmotor1.motor_rotate(0)
                time.sleep(0.1)
                break
    for i in range(0,3):
        Lightwork(2, "green")
        time.sleep(1.3)
        Lightwork(2, "off")
        time.sleep(0.3)
    setmotor1.motor_rotate(-20)
    time.sleep(0.6)
    setmotor1.motor_rotate(0)
    print("raiseflag stop!")


def shot_target(motor_port):
    print("shot_target start!")
    setmotor1 = Motor_rotate(motor_port)
    setmotor1.motor_rotate(40)
    time.sleep(1)
    setmotor1.motor_rotate(0)
    time.sleep(0.1)
    setmotor1.motor_rotate(-40)
    time.sleep(0.9)
    setmotor1.motor_rotate(0)
    print("shot_target stop!")

def shot_target1(motor_port):
    print("shot_target start!")
    setmotor1 = Motor_rotate(motor_port)
    setmotor1.motor_rotate(40)
    time.sleep(0.7)
    setmotor1.motor_rotate(0)
    time.sleep(0.1)
    setmotor1.motor_rotate(-45)
    time.sleep(0.75)
    setmotor1.motor_rotate(0)
    print("shot_target stop!")

def capture_target(servo485ID,servoPWMID):
    servo1=Servo(servo485ID)
    servo2=Servo_pwm(servoPWMID)
    servo1speed=70
    servo2speed=80
    servo2.servocontrol(180, servo2speed)
    time.sleep(0.5)
    servo1.servocontrol(-70, 70)
    time.sleep(0.5)
    servo2.servocontrol(95, servo2speed)
    time.sleep(0.5)
    servo1.servocontrol(0,servo1speed)
    time.sleep(0.5)

def banyun(motor_port):
    print("banyun start!")
    setmotor1 = Motor_rotate(motor_port)
    time.sleep(0.1)
    setmotor1.motor_rotate(12)
    time.sleep(1)
    setmotor1.motor_rotate(0)
    time.sleep(0.8)
    setmotor1.motor_rotate(-15)
    time.sleep(0.8)
    setmotor1.motor_rotate(0)
    print("banyun stop!")
def Lightwork(light_port,color):
    light=Light(light_port)
    red=[80,0,0]
    green=[0,80,0]
    yellow=[80,80,0]
    off=[0,0,0]
    light_color=[0,0,0]
    if color =='red':
        light_color=red
    elif color=='green':
        light_color=green
    elif color=='yellow':
        light_color=yellow
    elif color=='off':
        light_color = off
    light.lightcontrol(0,light_color[0],light_color[1],light_color[2])
def buzzer():
    buzzer=Buzzer()
    for i in range(1,10):
        # print(i)
        buzzer.rings()
        time.sleep(0.5)

# from thserial import Recv_threading
if __name__ == '__main__':

    banyun(1)

