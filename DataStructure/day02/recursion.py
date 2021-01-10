"""
    归并排序
"""
li = [12,8,3,5,4,6,7,2,88]

def merge_sort(li):
    mind = len(li) // 2
    if len(li) == 1:
        return li
    left = li[:mind]
    right = li[mind:]
    left_li = merge_sort(left)
    right_li = merge_sort(right)
    return merge(left_li,right_li)

def merge(left_li,right_li):
    result = []
    while len(left_li) > 0 and len(right_li) >0:
        if left_li[0] >= right_li[0]:
            result.append(right_li.pop(0))
        else:
            result.append(left_li.pop(0))
    result += left_li
    result += right_li
    return result

if __name__ == '__main__':
    print(merge_sort(li))
    print(li)
