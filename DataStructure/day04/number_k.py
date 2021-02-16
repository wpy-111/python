"""
    输入一个链表，输出该链表中倒数第k个节点
    思路：
        1.遍历链表，把每个节点都放到列表中
        2.利用列表的负索引获取倒数第k个节点
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Solution:
    def get_k_node(self,head,k):
        li = []
        cur = head
        while cur:
            li.append(cur)
            cur = cur.next

        if k < 0 or k > len(li):
            raise IndexError('list index out of range')
        return li[-k]


if __name__ == '__main__':
    #创建一个链表
    s = Solution()
    node = Node(100)
    node.next = Node(200)
    node.next.next = Node(300)
    print(s.get_k_node(node,8).value)










