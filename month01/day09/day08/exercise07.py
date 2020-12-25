"""
    二分查找：
    定义函数，再有序数字列白中找到目标值，并返回其索引
    如果目标值不在列表中，返回他可以按顺序插入的索引
    输入:[1,2,6,8,9]  8
    输出：3
    输入：[1,2,6,8,9]  5
    输出：2
"""
list01=[1,2,6,8,10]
def binary_search(list,target):
    left=0
    right = len(list)
    while left<= right:
        mid=(left+right)//2
        if list[mid]==target:
            return mid
        elif list[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left
print(binary_search([1,2,6,7,8],5))








