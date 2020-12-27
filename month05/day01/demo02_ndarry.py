"""
   demo01 ndarray对象操作
   标量是一个数字，向量是一组数
   向量与向量相加对应位置做运算
"""
import numpy as np
#二维列表
#nuppy.array()
ary = np.array([[1,2,3,4,5],
               [2,5,6,9,10]])
print(ary,ary.shape,ary.dtype)
ary = np.array([[1,5,6,8,9]])
print(ary,ary.shape)
#nuppy.arange()
ary2 = np.arange(0,10,2)
print(ary2)
#numpy.zeros()
ary3 = np.zeros(10,dtype='int32')
ary4 = np.zeros((2,4),dtype='int16')
print(ary3,ary3.shape,ary3.dtype)
print(ary4,ary4.shape)
#numpy.ones()
ary5 = np.ones((2,4),dtype='float32')
ary6 = np.ones((2,4),dtype='bool')
print(ary5)
print(ary6)
#numpy.zeros_like() numpy.ones_like()
print(np.zeros_like(ary4))
print(np.ones_like(ary4))





