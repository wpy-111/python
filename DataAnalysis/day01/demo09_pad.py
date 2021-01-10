"""
    添加元素
"""
import numpy as np
ary = np.arange(1,5)
print(ary)
ary = np.pad(ary,pad_width=(2,2),mode='constant',constant_values=-1)
print(ary)

#两个一维数组变成一个两行的数组
a = np.arange(1,9)
b = np.arange(9,17)
ary = np.row_stack((a,b))
print(ary)
ary = np.column_stack((a,b))
print(ary)

