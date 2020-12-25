"""
queue_test.py演示模块
"""
from multiprocessing import Queue,Process
from time import sleep
from random import randint
#创建消息队列
q = Queue(3)
def handle():
    while True:
        try:
            data = q.get(timeout=8)
        except Exception as e:
            print(e)
            break
        else:
            print('%d + %d ='%(data[0],data[1]),data[0]+data[1])
def request():
    for i in range(6):
        sleep(randint(1,12))
        x = randint(1,100)
        y = randint(1,100)
        q.put((x,y))
p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()