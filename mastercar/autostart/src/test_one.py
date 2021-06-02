from widgets import Motor_rotate
import time
a = Motor_rotate(2)
a.motor_rotate(20)
time.sleep(1)
a.motor_rotate(0)
a.motor_rotate(-20)
time.sleep(1)
a.motor_rotate(0)