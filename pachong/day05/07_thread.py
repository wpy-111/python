"""
   多线程实例
"""
from threading import Thread
list = []
#线程1
def f1():
    print("我是发1")

t = Thread(target=f1)
t.start()

for i in range(0,5):
    t = Thread(target=f1)
    list.append(t)
    t.start()
for i in list:
    i.join()