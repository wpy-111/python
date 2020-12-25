#练习1.使用迭代思想，获取元祖中所有元素（“a","b","C")
#练习2.使用迭代思想，获取字典中所有记录（“a"：1,"b"：2,"C"：3)
tuple=("a","b","C")
iteration=tuple.__iter__()
# while True:
while True:
    try:
        item=iteration.__next__()
        print(item)
    except StopIteration:
        break
dict={"a":1,"b":2,"c":3}
iterations=dict.__iter__()
while True:
    try:
        qtx=iterations.__next__()
        value=dict[qtx]
        print("%s:%s"%(qtx,value))
    except StopIteration:
        break