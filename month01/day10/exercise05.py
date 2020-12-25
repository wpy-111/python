"""
   对象计数器
   创建老婆类，记录老婆对象的数量
"""
class Wife:
    count=0
    def __init__(self,name):
        self.name=name
        Wife.count+=1
w01=Wife("消防")
w02=Wife("小妹")
w03=Wife("小李")
print(Wife.count)