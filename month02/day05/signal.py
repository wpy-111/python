"""
    signal避免产生僵尸进程
"""
from os import *
from signal import *
from time import sleep
signal(SIGCHLD,SIG_IGN)#非阻塞，不会影响父进程进行，可以处理所有子进程退出
pid = fork()
if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print('Child PID:',getpid())
else:
    print('Parent PID:',getpid())
    while True:
        pass