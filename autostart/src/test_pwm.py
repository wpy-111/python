from obstacle import *
from widgets import *
servo1 = Servo_pwm(2)
servo1speed = 50
servo2speed = 50
time.sleep(1)
servo1.servocontrol(3, servo1speed)
time.sleep(3)
#servo1.servocontrol(90,servo1speed)
#time.sleep(3)
servo1.servocontrol(114, servo1speed)
time.sleep(3)
servo1.servocontrol(114,50)
time.sleep(2)