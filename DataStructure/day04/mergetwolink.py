"""
    合并两个链表
    输入两个单调递增的链表，输出两个链表合成后的链表，满足单调递增的特点
    思路：
        1.最终返回合并后的链表头节点
        2.先确定新链表的头节点
        3.互相比较，移动小游标
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Solution:
    def merge_two_link(self,head1,head2):
        #确定新链表的表头
        if head1 and head2:
            if head1.value > head2.value:
                merge_head = head2
                head2 = head2.next
            else:
                merge_head = head1
                head1 = head1.next
            p = merge_head

        elif head1:
            return head1
        else:
            return head2

        #开始遍历   进行合并
        while head1 and head2:
            if head1.value <= head2.value:
                merge_head.next = head1
                head1 = head1.next
            else:
                merge_head.next = head2
                head2 = head2.next
            merge_head = merge_head.next
        if head1:
            merge_head.next = head1
        else:
            merge_head.next = head2
        #返回合并后链表的头节点
        return p
if __name__ == '__main__':
    s = Solution()
    n100 = Node(100)
    n200 = Node(200)
    n300 = Node(300)
    n400 = Node(400)
    n666 = Node(666)
    n888 = Node(888)
    n200_2 = Node(200)
    n1 = Node(1)
    head1 = n100
    n100.next = n200
    n200.next = n300
    n300.next = n400
    head2 = n1
    n1.next = n200_2
    n200_2.next = n666
    p = s.merge_two_link(head1,head2)
    print(p.value)


