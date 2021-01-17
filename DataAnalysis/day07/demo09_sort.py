"""
    排序相关的有关方法
"""
import numpy as np
products = np.array(["Apple", "Huawei", "Mi", "Oppo", "Vivo"])
prices = np.array([8888, 5888, 2999, 3999, 3999])
volumns = np.array([60, 110, 40, 50, 70])
#先按照价格排序再按价格排序
#indices = numpy.lexsort((参考序列, 待排序列))
sorted_index = np.lexsort((-volumns,prices))
print(products[sorted_index])
#插入排序 a 是有序数组
a = np.array([1,3,4,5,7])
b = np.array([2,6])
index = np.searchsorted(a,b)
print(index)
c = np.insert(a,index,b)
print(c)





