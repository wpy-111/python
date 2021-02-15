"""
    python实现队列模型，使用链式存储结构
    思路：
        1.队列：先进先出
        2.设计：链表的尾部最为队尾，进行入队操作，相当于在链表尾部添加一个节点
                链表的头部作为队头，进行出队操作，相当于删除链表头节点
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        #创建空队列头节点为None
        self.head = None

    def is_empty(self):
        return self.head == None

    def enqueue(self,value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = node

    def dequeue(self):
        if self.is_empty():
            raise Exception('dequeue from empty queue')
        cur = self.head
        self.head = self.head.next

        return cur.value

    def size(self):
        if self.is_empty():
            return 0
        count = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            count += 1

        return count

if __name__ == '__main__':
    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    print(q.size())
    print(q.dequeue())
    print(q.size())


