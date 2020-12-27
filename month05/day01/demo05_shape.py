"""
   维度操作
"""
import numpy as np
ary = np.arange(1,9)
print(ary,ary.shape)
b = ary.reshape(2,4)
print(b,b.shape)
ary[0] = 999
print(b)
#ravel()变为一维数图
c = b.ravel()
print(c)
#复制变维
d = c.flatten()
c[0] = 12
print(d,d.shape)
print(c)


