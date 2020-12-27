"""
  attr.py
"""
import numpy as np
#注意19不算
ary = np.arange(1,19)
print(ary,ary.shape)
ary.shape = (3,6)
print(ary,ary.shape)
ary.shape = (2,3,3)
print(ary,ary.shape)

#dtype
ary1 = np.arange(1,7)
print(ary1,ary1.dtype)
ary2 = ary1.astype('int64')
ary1.dtype = 'float32'
#astype有返回值 创建新对象
print(ary1,ary1.dtype)
print(ary2,ary2.dtype)

#size  reshape设置维度
ary3 = np.arange(1,9).reshape(2,4)
print(ary3,ary3.shape,ary3.size,len(ary3))
#[[1 2 3 4]
#[5 6 7 8]] (2, 4)   8   2

#索引访问
ary4 = np.arange(1,9).reshape(2,2,2)
print(ary4,ary4.shape)
print('------')
print(ary4[0])
print(ary4[0][0])
print(ary4[0][0][0])
print(ary4[0,0])
print(ary4[0,0,0])
for i in range(ary4.shape[0]):
    for j in range (ary4.shape[1]):
        for k in range(ary4.shape[2]):
            print(ary4[i,j,k],end= '\t')




