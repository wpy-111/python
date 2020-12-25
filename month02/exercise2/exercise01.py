"""
写两个线程，一个线程打印1-52,另一个线程打印A-Z要求打印顺序为12A34B.....，
不能使用sleep
"""
from threading import Thread,Lock
lock1 = Lock()
lock2 = Lock()
def print_number():
    for item in range(1,53,2):
        lock1.acquire()
        print(item,item+1,end="")
        lock2.release()

def print_letter():
    list = ["A","B","C","D","E","F","G","H","I","J","K"
            ,"L","M","N","O","P","Q","R","S","T","U","V"
            ,"W","X","Y" ,"Z"]
    for item in list:
        lock2.acquire()
        print(item ,end="")
        lock1.release()
t1 = Thread(target=print_number)
t2 = Thread(target=print_letter)
lock2.acquire()#def print_letter():堵塞
t1.start()
t2.start()
t1.join()
t2.join()