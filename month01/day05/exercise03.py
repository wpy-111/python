"""
    在列表[5,6,17,78,34,5]
    删除大于10的元素
    温馨提示:调试/画图
"""
# 倒序删除
list_result = [5, 6, 17, 78, 34, 5]
for txm in range(len(list_result) - 1, -1, -1):
    if list_result[txm] > 10:
         del list_result[txm]

print(list_result)