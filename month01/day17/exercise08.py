
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
           Wife("铁钉",182,50,26),]
"""
    练习：
    定义函数，在老婆列表中查找年龄大于25的所有老婆对象
    定义函数，在老婆列表中查找身高小于180的所有老婆对象
"""

def find(tareget,fun):
    for item in tareget:
        if fun(item):
            yield item

def contion01(item):
    return item.age>25
def contion02(item):
    return item.length<180
for item in find(list_Wife,contion02):
    print(item)
