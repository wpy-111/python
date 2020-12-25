"""
   顺序存储的方式实现队列
   列表的尾部作为队尾，进行入队操作 ——append（）
   列表的头部作为队头，进行出队操作 ——pop（0）
"""
class Queue:
    def __init__(self):
        #创建空队列
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def inqueue(self, value):
        self.elems.append(value)
    def dequeuq(self):
        """出队操作"""
        if self.is_empty():
            raise Exception("Dequeue From Empty Queue")
        return self.elems.pop(0)
if __name__ == '__main__':
    s = Queue()
    s.inqueue(100)
    s.inqueue(200)
    s.inqueue(300)
    print(s.dequeuq())