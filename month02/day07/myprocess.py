"""
  自定义进程类
"""
from multiprocessing import Process
from time import sleep,ctime
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()
    def fun01(self):
        sleep(1)
        print('第一步')
    def fun02(self):
        sleep(0.8)
        print('第二步')

    #调用start会执行run，作为进程
    def run(self):
        for i in range(self.value):
            self.fun01()
            self.fun02()
c=MyProcess(2)
c.start()
c.join()
