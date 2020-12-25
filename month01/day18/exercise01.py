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
           Wife("铁钉",182,50,26),]
"""
   需求：
   1.定义函数，在老婆列表中查找所有的老婆姓名
   2.定义函数，在老婆列表中查找所有的老婆姓名和身高
"""
#步骤
    # 1.将需求完整的实现到函数中
    # 2.将变化点单独定义到函数中
    # 3.将通用代码定义到函数中
    # 4.用参数隔离变化点
    # 5.将通用代码移动到IterableHelper类中
    # 6.测试调用IterableHelper的静态方法执行功能

def conditon01(item):
    return  item.name
def conditon02(item):
    return  (item.name,item.length)

for item in IterableHelper().find_all(list_Wife,conditon02):
    print(item)
re=map(lambda item:(item.name,item.length),list_Wife)
for item in re:
    print(item)



