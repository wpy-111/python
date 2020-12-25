"""
   线程锁
"""
from threading import Thread,Lock
lock = Lock()
n = 5000
def f1():
    global n
    for i in range(1000000):
        lock.acquire()
        n = n+1
        lock.release()

def f2():
    global  n
    for i in range(1000000):
        lock.acquire()
        n = n - 1
        lock.release()


t = Thread(target=f1)
t.start()

t1 = Thread(target=f2)
t1.start()
t.join()
t1.join()
print(n)

















