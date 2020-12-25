"""
    创建老婆类
      定义函数老婆列表中查找身高在160--170之间打所有老婆
      定义函数老婆列表中查找年龄在25--30之间的所有老婆姓名和年龄
"""
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
           Wife("小马",166,55,28),
           Wife("小秀",162,52,26),
           Wife("铁钉",162,50,26),]
def find_length_wife():
    for item in list_Wife:
        if 160<=item.length<=170:
            yield item
for item in find_length_wife():
    print(item)
generator=list(find_length_wife())
print(generator[1])
for item in generator:
    print(item)
# 定义函数老婆列表中查找年龄在25 - -30之间的所有老婆姓名和年龄
def find_age_wife():
    for item in list_Wife:
        if 25<=item.age<=30:
            yield (item.name,item.age)
for item in find_age_wife():
    print(item)

#--定义函数，在老婆列表中查找铁钉老婆对象
def find01():
    for item in list_Wife:
        if item.name=="铁钉":
            return item
print(find01())
#---------------------------------------
#--定义函数，在老婆列表中查找体重在40-60之间的所有老婆
def find02():
    for item in list_Wife:
        if 40<=item.weight<=60:
            yield item
# for item in find02():
#     print(item)
print("-------")
generator=list(find02())
print(generator[2])


