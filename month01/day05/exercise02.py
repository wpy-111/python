"""
   练习 在列表中找出最大打元素
"""
list=[1,52,65,858,85,99,548]
max_height =list[0]
for i in range(1,len(list)):
    if max_height <= list[i] :
        max_height = list[i]
print(max_height)

