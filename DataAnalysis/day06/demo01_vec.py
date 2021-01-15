"""
    函数矢量化
"""
import numpy as np
import math
def func(x,y):
    return math.sqrt(x**2 + y**2)
a,b = np.array([4,3,3]),np.array([4,4,6])
#使用vectorize，对func函数执行函数矢量化，这样就可以处理矢量数据
fun_vec= np.vectorize(func)
print(fun_vec(a,b))
print(fun_vec(a,4))
print(np.sqrt([9+16,9+16]))