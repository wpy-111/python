"""
 Process 进程创建方法
"""

import multiprocessing as mp
from time import sleep

def fun01():
    sleep(2)
    print("子进程函数")
#实例化进程对象
p=mp.Process(target=fun01)
if __name__ == '__main__':
    p.start()#启动进程，执行target绑定函数
    p.join()#回收进程