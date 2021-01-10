"""
    使用链式结构实现 栈
"""
# 链表栈模型
from singlelink import Node, Singlelinklist
class Stack:
    def __init__(self):
        self.link=Singlelinklist()
    def is_empty(self):
        self.link.is_empty()
    def push(self,value):
        self.link.add(value)
    def pop(self):
        self.link.remove(self.link.head.value)
    def top(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise Exception("pop from empty stack")
        return self.link.head.value
if __name__ == '__main__':
    s=Stack()
    s.push(100)
    s.push(200)
    s.push(300)
    s.pop()
    s.pop()
    s.pop()
