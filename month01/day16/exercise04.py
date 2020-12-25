#   练习：
#   定义图形管理器，记录多个图形
#    迭代图形管理器，获取多个图形
class ShapeIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]


class ShapeManager:

    def __init__(self):
        self.__list_shape = []

    def add_shape(self, skill):
        self.__list_shape.append(skill)

    def __iter__(self):
        return ShapeIterator(self.__list_shape)


manager = ShapeManager()
manager.add_shape("圆形")
manager.add_shape("长方形")
manager.add_shape("球形")

for item in manager:
    print(item)
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
