"""
   模拟死锁产生的过程
"""
from time import sleep
from  threading import Thread,Lock
#账户类
class Accont:
    def __init__(self,_id,balanace,lock):
        self.id = _id#账户名
        self.balanace = balanace#账户金额
        self.lock = lock# 锁
    #取钱
    def withdraw(self,amount):
        self.balanace -= amount
    #存钱
    def deposit(self,amount):
        self.balanace +=amount
    #查看于额
    def get_balanace(self):
        return self.balanace
Tom =Accont("Tom",5000,Lock())
Alex =Accont("Alex",8000,Lock())

def transfer(from_,to,amount):
    """
    :param from_: 从该账户转钱
    :param to: 给这个账户转入
    :param amount: 转入金额
    :return:
    """
    from_.lock.acquire()#from_上锁
    from_.withdraw(amount)
    from_.lock.release()
    to.lock.acquire()#to上锁
    to.deposit(amount)
    to.lock.release()
t1 = Thread(target=transfer,args=(Tom,Alex,2000))
t2 = Thread(target=transfer,args=(Alex,Tom,1000))
t1.start()
t1.join()
print(Tom.get_balanace())
print(Alex.get_balanace())
