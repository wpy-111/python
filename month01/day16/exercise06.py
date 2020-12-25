"""
    练习：
        自定义MyRange类，实现下列效果
"""
class MyRangeIterator:
    def __init__(self,end):
        self.__end=end
        self.__counter=0
    def __next__(self):
            if self.__end == self.__counter:
                raise StopIteration
            item= self.__counter
            self.__counter+=1
            return item

class MyRange:
    def __init__(self,figuer):
        self.figuer=figuer
    def __iter__(self):
        return MyRangeIterator(self.figuer)
c01=MyRange(5)
for item in c01:
    print(item)