"""
   线程创建实例
"""
from threading import Thread
from time import sleep
#含有参数的线程函数
def fun(sec,name):
    print('线程函数参数')
    sleep(sec)
    print("%s执行完毕"%name)
#创建五个线程
job = []
for item in range(5):
    t = Thread(target=fun,args=(2,),kwargs={'name':'T%d'%item})
    job.append(t)
    t.start()
for i in job:
    i.join()


