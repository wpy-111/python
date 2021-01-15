"""
    numpy通用函数
"""
import numpy as np
ary = np.arange(1,10)
# 将调用数组中小于和大于下限和上限的元素替换为下限和上限，返回裁剪后的数组，调用数组保持不变。
print(ary.clip(min=3,max=7))
# 返回由调用数组中满足条件的元素组成的新数组。
print(ary.compress(ary>3))
# 返回数组的符号数组
print(np.sign(ary))

