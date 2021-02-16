"""
    输入一个链表，反转链表后，输出新链表的表头
    思路：
        1.特殊情况：空链表和一个节点
        2.建立两个游标：保存上一个节点和保存要操作的节点
        3.代码逻辑
            当前节点指针指向上一个节点
            两游标往后移
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Soultion:
    def get_reverse_head(self,head):
        #特殊情况空列表
        if head is None:
            return print("The link is empty")
        #特殊情况只用一个节点
        if head.next == None:
            return head

        cur = head
        pre = None
        while cur:
            #next_node下一个要操作的节点
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
if __name__ == '__main__':
    s = Soultion()
    node = Node(100)
    node.next = Node(200)
    node.next.next = Node(300)
    new_link = s.get_reverse_head(node)
    cur = new_link
    while cur:
        print(cur.value,end=' ')
        cur = cur.next





