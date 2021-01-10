
"""
   python实现单链表
"""
class Node:
    """
      结点类
    """
    def __init__(self, value):
        self.value=value
        self.next = None

class Singlelinklist:
    """  单链表类"""
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None

    def length(self):
        """获取链表的长度"""
        current = self.head
        count = 0
        while current!= None:
            count += 1
            current = current.next
        return count
    def travel(self):
        """遍历整个链表"""
        current = self.head
        while current != None:
            print(current.value,end=" ")
            current = current.next
        print()
    def add(self,value):
        """在链表头部添加结点"""
        if self.is_empty():
            self.head = Node(value)
        else:
            node=Node(value)
            node.next = self.head
            self.head = node
    def insert(self,pos,value):
        """
           在指定位置添加元素
        :param pos: 指定添加的位置
        :param value: 添加的值
        :return:
        """
        if pos < 0:
            self.add(value)
        elif pos > self.length():
            self.append(value)
        else:
            node = Node(value)
            pre = self.head
            count = 0
            while pos-1 > count:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def append(self,value):
        """
           在链表尾部添加结点
           特殊情况：链表为空
        """
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            node.next = None
    def remove(self,value):
        """删除元素"""
        current = self.head
        pre = None
        while current!= None:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                else:
                    pre.next = current.next
                break
            else:
                pre = current
                current = current.next
    def search(self,value):
        """查找在链表中是否存在"""
        current = self.head
        while current != None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False


if __name__ == '__main__':
    s = Singlelinklist()
    print(s.length())
    s.travel()
    s.add(200)
    s.add(100)
    s.travel()
    s.append(300)
    s.append(400)
    s.travel()
    s.insert(2,666)
    s.travel()
    print(s.search(200))
    s.remove(200)
    s.travel()

