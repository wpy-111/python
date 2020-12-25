"""
    练习：在不改变fun01与fun02函数定义和调用的情况下，
    为其增加新功能（打印函数执行时间）
"""
#装饰器
import time
def print_execute_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        re=func(*args,**kwargs)
        stop_time=time.time()
        print(stop_time-start_time)
        return re
    return wrapper
def print_name(func):
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return func(*args,**kwargs)
    return wrapper
@print_execute_time
@print_name
def fun01():
    print("hello")
    time.sleep(2)
@print_name
def fun02():
    time.sleep(3)
fun01()
fun02()
#猜测先进行新功能（由近及远）在进行旧功能