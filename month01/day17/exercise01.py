"""
   练习：
      定义员工管理器，记录多个员工
      迭代员工管理器，获取多个员工
      要求：体会推导过程
              调试
     变化 将迭代器版本，改为yield版本
     调试
"""

class StraffManager:
    def __init__(self):
        self.__list_straff = []

    def add_straff(self,target):
        self.__list_straff.append(target)

    def __iter__(self):
        index=0
        while index < len(self.__list_straff):
            item=self.__list_straff[index]
            yield item
            index+=1



c01 = StraffManager()
c01.add_straff("程序员")
c01.add_straff("员工")
c01.add_straff("清洁工")

for item in c01:
    print(item)
