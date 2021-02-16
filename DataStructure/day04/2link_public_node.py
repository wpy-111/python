"""
    输入两个链表，找出他们的第一个公共的节点  节点后面必选完全相同
    思路：
        1.从公共节点开始，后面两个链表的节点一定相同
        2.创建两个列表，分别存放放个链表的节点对象
        3.从两个列表从后往前判断，到最后一个公共节点时返回
        4.判断两个对象是否为同一个 a is b
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Solution:
    def get_first_public_node(self,head1,head2):
        #先把两个链表中节点添加到列表中
        list1 = []
        list2 = []
        cur1 = head1
        cur2 = head2
        while cur1:
            list1.append(cur1)
            cur1 = cur1.next
        while cur2:
            list2.append(cur2)
            cur2 = cur2.next
        node = None
        #从后往前判断  保证list存在
        while list2 and list1 and list1[-1] is list2[-1]:
            node = list1.pop()
            list2.pop()
        return node

if __name__ == '__main__':
    s = Solution()
    n100 = Node(100)
    n200 = Node(200)
    n300 = Node(300)
    n400 = Node(400)
    n666 = Node(666)
    n888 = Node(888)
    node1 = n100
    n100.next = n200
    n200.next = n300
    n300.next = n400

    node2 = n666
    n666.next = n888
    n888.next = n300
    n300.next = n400
    #测试方法
    print(s.get_first_public_node(node1,node2).value)
