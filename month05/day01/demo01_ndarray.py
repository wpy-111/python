"""
   demo01 ndarray对象操作
   标量是一个数字，向量是一组数
   向量与向量相加对应位置做运算
"""
import numpy as np
#一维数组
ary = np.array([1,5,6,56])
print(ary,type(ary))
print(ary * 10)
print(ary > 10)
print(ary + ary)
print(ary * ary)




