"""
    模拟僵尸进程的产生
"""
import os, sys

pid = os.fork()
if pid < 0:
   print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
else:
    pid,statue=os.wait()
    print("PID:",pid)
    print("STATUE:",statue)
    while True:
        pass