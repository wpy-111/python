"""
    在一个有序的链表中，存在重复的节点，请删除链表中重复的节点，重复的节点保留一个，返回链表头指针
    思路：
        1.从头开始，往后遍历一次比较当前节点和下一个节点数据区元素是否相等
        2.相等：current = current.next 移动游标
        3.不相等删除节点：current.next = current.next.next
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Solution:
    def del_repeat_node(self,head):
        #空链表
        if head is None or head.next is None:
            return head
        #正常的情况
        cur = head
        while cur.next and cur:
            if cur.value == cur.next.value:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

if __name__ == '__main__':
    s = Solution()
    n100 = Node(100)
    n200 = Node(200)
    n200_2 = Node(200)
    n300 = Node(300)
    head = n100
    n100.next = n200
    n200.next = n200_2
    n200_2.next = n300

    new_head = s.del_repeat_node(head)
    print(new_head.value)
    cur = new_head
    while cur:
        print(cur.value,end=' ')
        cur = cur.next








