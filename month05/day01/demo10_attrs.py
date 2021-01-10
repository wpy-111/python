"""
   属性操作
"""
import numpy as np
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)#维数
print(a.itemsize)#每一个元素站的字节
print(a.nbytes)#
print(a.real)
print(a.imag)
print(a.T)
print([element for element in a.flat])
print(a.tolist())
#列表推导式[i for i in range(1,10)]

