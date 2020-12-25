from time import sleep
import os,sys
def fun01():
    for i in range(3):
        sleep(2)
        print("写代码")
def fun02():
    for i in range(2):
        sleep(4)
        print("刷代码")
pid=os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    spid=os.fork()
    if spid < 0:
        print('Error')
    elif spid == 0:
        fun02()#二级子进程
    else:
        os._exit(0)
else:
    os.wait()
    fun01()