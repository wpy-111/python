"""
   demo07_mask 掩码操作
"""
import numpy as np
a = np.arange(1,10)
mask = a % 2 == 1
print(a)
print(mask)
print(a[mask])
a[mask] = 999
print(a)
a = np.arange(1,100)
print(a[(a%7==0)&(a%3==0)])

#索引掩码
product = np.array(['Mi','Oppo','Vivo','Apple','HuaWei'])
sort_indices = [0,2,1,4,3]
print(product[sort_indices])

