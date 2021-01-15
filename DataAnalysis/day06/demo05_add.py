"""
    加法通用函数
"""
import numpy as np
ary = np.arange(1,7)
print(np.add(ary,ary))#数组对应位置相加
print(np.add.reduce(ary))#数组累加
print(np.add.accumulate(ary))#累加过程
print(np.add.outer([10,20,30],ary))#ary作为列标签和前面相加

print(np.prod(ary))#累乘的结果
print(np.cumprod(ary))#累乘的过程
print(np.outer([10,20,30],ary))#ary作为列标签和前面累乘
