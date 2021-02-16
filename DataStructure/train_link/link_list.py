"""
    输入一个链表，按链表从未到头的顺序返回一个 Arrylist
    思路：
        1.链表只能从头到尾遍历，不能从未到头
        2.把试题转为更好操作的数据类型
        3.从头到尾遍历，把数据区存入到列表中【100，200，300】
        4.在利用列表的方法进行反转
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
#方法一：
# class Soution:
#     def revers_link_list(self,head):
#         arry_list = []
#         cur = head
#         while cur:
#             arry_list.append(cur.value)
#             cur = cur.next
#
#         #进行列表的反转
#         arry_list.reverse()
#         return arry_list
#方法二：
class Soution:
    def revers_link_list(self,head):
        arry_list = []
        cur = head
        while cur:
            arry_list.insert(0,cur.value)
            cur = cur.next
        #进行列表的反转
        return arry_list
if __name__ == '__main__':
    s = Soution()
    head = Node(100)
    head.next= Node(200)
    head.next.next= Node(300)
    print(s.revers_link_list(head))












