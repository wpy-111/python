"""
    定义函数，在老婆列表中找出年龄最大的老婆
    定义函数，在老婆列表中找出身高最高的老婆
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
           Wife("小秀",162,52,24),
           Wife("铁钉",182,50,26),]

re=IterableHelper.find_most(list_Wife,lambda a:a.length)
print(re)
"""
    定义函数，在老婆列表中将老婆身高进行排序
    定义函数，在老婆列表中将老婆体重进行排序
"""
IterableHelper.ascending(list_Wife,lambda a:a.length)
for item in list_Wife:
    print(item)
re=sorted(list_Wife,key=lambda a:a.length,reverse=True)
for itx in re:
    print(itx)