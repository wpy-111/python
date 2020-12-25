# 用函数做升序
def ascending(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r+1, len(list_target)):
            if list_target[c] < list_target[r]:
                list_target[c], list_target[r]= list_target[r], list_target[c]

list_result=[1, 9, 8, 5, 65, 74, 646, 123, 47, 865, 12, 35]
ascending(list_result)
print(list_result)