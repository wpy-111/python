"""
   冒泡排序
"""
list = [9,5,322,54,18,65,121,566,48,4894,1651,2222]
for item in range(len(list)-1):
    for r in range(item+1,len(list)):
        if list[item] > list[r]:
            list[item],list[r] = list[r],list[item]
print(list)
