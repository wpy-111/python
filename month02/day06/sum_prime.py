"""
   计算质数的和
"""
import time
from multiprocessing import Process
def print_time(sum_prime):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        re = sum_prime(*args,**kwargs)
        stop_time=time.time()
        print(stop_time-start_time)
        return re
    return wrapper
@print_time
def sum_prime(number1,number2):
    if number1 <= 1:
        return False
    for i in range(number1,number2):
        pass
        # if n % i == 0:
        #     i +=
sum_prime(1,10000)
p = Process(target=sum_prime,args=(2,2500,))
s = Process(target=sum_prime,args=(2501,5000,))
c = Process(target=sum_prime,args=(5001,7500,))
x = Process(target=sum_prime,args=(7501,10000,))
p.start()
s.start()
c.start()
x.start()
p.join()
s.join()
c.join()
x.join()


