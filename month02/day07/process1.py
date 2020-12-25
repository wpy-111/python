import time
from multiprocessing import Process
def print_time(fun):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        re = fun(*args,**kwargs)
        end_time = time.time()
        print("%s消耗%.6f"%(fun.__name__,end_time-start_time))
        return re
    return wrapper
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
@print_time
def sum_prime(number01,number02):
    prime = []
    for i in range(number01,number02):
        if is_prime(i):
            prime.append(i)
    sum(prime)
class Prime(Process):
    def __init__(self,begin,end):
        super().__init__()
        self.prime = []
        self.begin = begin
        self.end = end
    def run(self):
        for i in range(self.begin,self.end):
            if is_prime(i):
                self.prime.append(i)
        sum(self.prime)
@print_time
def four_process():
    process = []
    for i in range(1,100001,25000):
        p = Prime(i,i+25000)
        process.append(p)
        p.start()
    [i.join() for i in process]
@print_time
def ten_process():
    process = []
    for i in range(1,100001,10000):
        p = Prime(i,i+10000)
        process.append(p)
        p.start()
    [i.join() for i in process]
if __name__ == '__main__':
    #运行时间27秒
    # sum_prime(1,100000)
    #15.861155
    four_process()
    #13.396016
    ten_process()