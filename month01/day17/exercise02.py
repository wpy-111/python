#   练习：
#   定义图形管理器，记录多个图形
#    迭代图形管理器，获取多个图形
#  变化 将迭代器版本，改为yield版本
#      调试

class ShapeManager:

    def __init__(self):
        self.__list_shape = []

    def add_shape(self, skill):
        self.__list_shape.append(skill)

    def __iter__(self):
       for item in  self.__list_shape:
           yield item

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
