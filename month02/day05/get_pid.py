"""
   获取进程的PID号
"""
import os,time
pid=os.fork()
if pid<0:
    print("Creat process failed")
elif pid == 0:
    time.sleep(1)
    print("child PID：",os.getpid())
    print("get parent PID:", os.getppid())
else:
    print("get child PID:",pid)
    print("parent PID：", os.getpid())