#重点  子进程会复制父进程的全部内存空间
#创建子进程
print("==================================")
a=1
import os
import time
pid=os.fork()
if pid<0:
    print("Creat process failed")
elif pid == 0:
    #子进程执行部分
    print("Child process")
    a=10000
    print('a=',a)
else:
    #父进程执行部分
    time.sleep(1)
    print("Parent process")
    print("a=",a)
print('ALL a=',a)