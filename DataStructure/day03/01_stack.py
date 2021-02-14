"""
    python 实现栈  用顺序存储方式实现栈
        思路：
            1.栈：后进先出 LIFO
            2.设计：顺序表（列表）实现，
                列表的头部作为栈底，append（）
                列表的尾部作为栈顶 pop（）
"""
class Stack:
    def __init__(self):
        #创建一个空栈
        self.stack = []

    def is_empty(self):
        """判断是否为空栈：空（True）非空（False）"""
        return self.stack == []

    def push(self,value):
        #相当于在列表的尾部添加元素
        self.stack.append(value)

    def pop(self):
        #相当于在列表的尾部删除一个元素
        if self.is_empty():
            raise Exception('pop from empty stack')
        return self.stack.pop()

    def size(self):
        #返回栈的大小
        return len(self.stack)

if __name__ == '__main__':
    s = Stack()
    s.push(100)
    s.push(200)
    s.push(300)
    s.push(400)
    s.push(500)
    s.pop()
    print(s.size())






















