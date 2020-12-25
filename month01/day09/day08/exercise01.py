"""
   练习1：定义函数，返回列表中不重复打元素（顺序不重要）
   输入:[4,35,7,64,7,35]
   输出：[4,35,7,64]
"""
def to_repeat(target):
    return list(set(target))
list01 = [4, 35, 7, 64, 7, 35]
print(to_repeat(list01))

