"""
    模拟生产，入库，销售场景
假定企业自产，自存，自销。将工厂生产的产品不定时的运到仓库，于此同时，仓库货物需要运到商场销售，
编写一个程序迷你这个过程（主要是对仓库的存取）
  *仓库可存量，可以设置为一个常量，比如max=10
  *仓库满的时候不能向仓库存入货物
  *仓库空的时候不能向商场提供货物
  *不能出现现存满再去或者先取完再存的情况
"""
from threading import Thread

class WareHouse(Thread):
    def __init__(self,information):
        super().__init__()
        self.warehouse=100
        self.information = information
    def run(self):
        if information[0] == 1:
            self.deposit(information[-1])
        elif information[0] == 2:
            self.take_goods(information[-1])
        elif information[0] == 3:
            self.find()
        else:
            print("输入错误")
    def deposit(self,size):
        if self.warehouse == 200:
            print("仓库已满不能存入东西")
            return
        else:
            if self.warehouse+size <=200:
                print("存入成功")
                print("已经存放%f件货物" % self.warehouse)
            else:
                print("存储失败")

            self.warehouse += size
    def take_goods(self,size):
        if self.warehouse == 0:
            print("货物已经没了")
        else:
            if self.warehouse - size < 0:
                print("货物数量不够")
                print("货物剩余%f件"%self.warehouse)
            else:
                print("取货成功")
    def find(self):
        print("货物一共有%f件"%self.warehouse)
while True:
    print("输入1存货 数量")
    print("输入2取货 数量")
    print("输入3查货")
    mes = input("请输入操作方式：")
    information = mes.split(" ")
    t = WareHouse(information)
    t.start()



