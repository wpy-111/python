"""
   线程对象属性
"""
from threading import Thread
from time import sleep
def fun():
    sleep(3)
    print("线程对象属性")
t = Thread(target=fun)
#主线程退出 分支线程也退出，必须写在start之前
t.setDaemon(True)
t.start()
#创建线程名称
# t.setName("Tedu")
print("name:",t.getName())
print("is alive:",t.is_alive())