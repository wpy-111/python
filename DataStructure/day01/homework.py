# 【2】输入一个链表，按链表值从尾到头的顺序返回一个 array_list
from singlelink import *
st=Singlelinklist()
st.add(200)
st.add(100)
st.append(300)
st.append(400)
st.travel()
def reverse_list():
    current = st.head
    list=[]
    while current != None:
        list.append(current.value)
        current = current.next
    return list[::-1]
print(reverse_list())
