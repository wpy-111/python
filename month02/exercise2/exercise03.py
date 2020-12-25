"""
模拟窗口卖票
有10个窗口（w1 ---w10），同时开放售票，一共50张票（T1-T50），按照顺序出售
要求输出每一张票的出售时间和窗口，不能出现票未出售或者出售多次的情况，窗口开放之前存放在容器中
1.使用多线程同步互斥的方法解决问题输出结果
2.每个线程模拟售票情景
3.将票的存储提前定一个合理的结构
"""
from threading import Thread,Lock
from time import ctime,sleep
list = []
for item in range(1,51):
    list.append("T"+str(item))
def ticket(name):
    while True:
        sleep(0.1)
        with Lock():
            if list:
                item = list.pop(0)
                print(name,"出售完一张票",item,ctime())
                continue
            return
jobs=[]
for item in range(1,11):
    t = Thread(target=ticket,args=("w"+str(item),))
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()

