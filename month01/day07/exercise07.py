"""
   一个筛子（1-6）
   打印出三个筛子所有数字
"""
list_result=[]
for i in range(1,7):
    for a in range(1,7):
        for c in range(1,7):
            list_result.append((a, i, c))
print(list_result)
print(len(list_result))
list_result=[(a, i, c) for i in range(1, 7) for a in range(1, 7) for c in range(1, 7)]
print(list_result)