"""
    定义函数，在老婆列表中累加所有老婆打总身高
    定义函数，在老婆列表中累加所有老婆的总体重
"""
from common.iterable_helper import IterableHelper


class Wife:
    def __init__(self, nane="", length=0, weight=0, age=0):
        self.name=nane
        self.length=length
        self.weight=weight
        self.age=age
    def __str__(self):
        return "%s--%d--%d--%d"%(self.name, self.length,self.weight,self.age)
list_Wife=[Wife("小王",156,100,29),
           Wife("小李",175,88,30),
           Wife("小张",170,66,20),
           Wife("小马",186,55,28),
           Wife("小秀",162,52,26),
           Wife("铁钉",182,50,24),]
#
# def accumulate01(item):
#      return item.length
# def accumulate02(item):
#     return item.weight
re=IterableHelper.accumulate(list_Wife,lambda item:item.weight)
print(re)
"""
    定义函数，在老婆列表中删除年龄在20-25之间的所有老婆
    定义函数，在老婆列表中删除体重大于60的所有老婆
"""
def condition01(item):
    return 20<=item.age<=25
def condition02(item):
    return  item.weight>60
re=IterableHelper.remove_all(list_Wife,lambda item:item.weight>60)
print(re)
for item in list_Wife:
    print(item)
# 定义函数，在老婆列表中查找体重大于60的所有老婆
for item in filter(lambda item:item.weight>60,list_Wife):
    print(item)

