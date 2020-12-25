"""
给进程函数传参
"""
from multiprocessing import Process
from time import sleep
#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print('我是%s'%name)
        print('I am working...')
#位置传参
# p = Process(target=worker,args=(2,'levi'))
# p = Process(target=worker,kwargs={'name':'lisa','sec':2})
p = Process(target=worker,args=(1,),kwargs={'name':'lisa'})
p.start()
p.join()