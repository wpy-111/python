import time
from widgets import *
setmotor1 = Motor_rotate(1)

time.sleep(0.5)
for i in range(0, 2):
    # setmotor1.motor_rotate(10)
    # time.sleep(3)
    setmotor1.motor_rotate(0)
    time.sleep(0.5)
    setmotor1.motor_rotate(-10)
    time.sleep(3)
    setmotor1.motor_rotate(0)
    time.sleep(0.5)