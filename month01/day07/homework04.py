"""
    定义函数在列表中查找最大值
"""
def find_max(list):
    max_value=list[0]
    for i in range(1,len(list)):
        if max_value< list[i]:
            max_value=list[i]
    return max_value
    # return max(list)
print(find_max([1,6,87,2,65,84,65]))