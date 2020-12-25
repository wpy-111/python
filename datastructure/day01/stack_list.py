#思路:
# 1. 利用列表完成顺序存储,但是列表功能多,不符合栈模型特点
# 2. 使用类将列表封装,提供符合栈特点的接口方法 """
# 顺序栈模型
class Stack:
    def __init__(self):
        self.element=[]
    def is_empty(self):
        """
        判断栈是否为空
        :return:
        """
        return self.element == []
    def push(self,value):
        """
          入栈
        :return:
        """
        self.element.append(value)
    def pop(self):
        """
          出栈
        :return:
        """
        if self.is_empty():
            raise  Exception("pop from empty stack")
        return self.element.pop()
    def top(self):
        """
           查看栈顶元素
        :return:
        """
        if self.is_empty():
            raise  Exception("pop from empty stack")
        return self.element[0]