from widgets import Motor_rotate
import time
a = Motor_rotate(4)
a.motor_rotate(100)
time.sleep(1)
a.motor_rotate(0)
a.motor_rotate(-100)
time.sleep(1)
a.motor_rotate(0)