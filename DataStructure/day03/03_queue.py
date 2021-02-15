"""
    python实现队列模型 - 顺序存储
    思路：
        1.先进先出
        2.设计：列表的头部最为队头pop（0），列表尾部最为队尾，进行入队操作append

"""
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self,value):

        return self.queue.append(value)

    def dequeue(self):

        if self.is_empty():
            raise Exception('dequeue from empty queue')
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
