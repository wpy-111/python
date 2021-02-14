"""
    python实现栈 - 使用链式结构
    思路：
        1.后进先出
        2.设计：链表的头部作为栈顶
               链表的底部作为栈底
        3.入栈：在链表的头部添加一个节点
          出栈：删除链表头节点
"""
class Node:
    """节点类"""
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        #创建一个空栈 设置链表的头节点为None
        self.top = None
    def is_empty(self):

        return self.top is None

    def push(self,value):
        """入栈操作：在链表头部添加一个节点"""
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """出栈操作：在链表的头部删除头节点"""
        if self.is_empty():
            raise Exception('pop from empty stack')
        pop_node = self.top
        top = self.top.next

        return pop_node.value

    def size(self):
        """栈大小：后去链表的长度"""
        if self.is_empty():
            return 0
        count = 0
        cur = self.top
        while not cur:
            cur = cur.next()
            count += 1 `



if __name__ == '__main__':









