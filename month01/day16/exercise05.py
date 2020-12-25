"""
   练习：
      定义员工管理器，记录多个员工
      迭代员工管理器，获取多个员工
      要求：体会推导过程
              调试
"""


class StraffIterator:
    def __init__(self, dete):
        self.index = 0
        self.date = dete
    def __next__(self):
        if self.index==len(self.date):
            raise StopIteration()
        else:
            item = self.date[self.index]
            self.index += 1
            return item
class StraffManager:
    def __init__(self):
        self.__list_straff = []

    def add_straff(self,target):
        self.__list_straff.append(target)

    def __iter__(self):
        return StraffIterator(self.__list_straff)


c01 = StraffManager()
c01.add_straff("程序员")
c01.add_straff("员工")
c01.add_straff("清洁工")
for item in c01:
    print(item)
