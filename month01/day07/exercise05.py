"""
    [5,65,98,23,115,35,14]
    升序（小---大0
    思想：
        取出前几个（不要最后一个)
        依次与后面的进行比较
        如果发现更小的则替换
"""
list_result = [5, 65, 98, 23, 115, 35, 14, 3]

# 取数据,做比较
for r in range(len(list_result) - 1):
    for c in range(r+1, len(list_result)):
        if list_result[c] < list_result[r]:
            list_result[c], list_result[r]= list_result[r], list_result[c]
        else:
            continue
print(list_result)
