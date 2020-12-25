"""
   线程基础使用
"""
import threading
from time import sleep
def fun():
    for i in range(3):
        sleep(2)
        print("播放黄河大合唱")

#创建线程对象
t = threading.Thread(target=fun)
#启动线程
t.start()
t.join()