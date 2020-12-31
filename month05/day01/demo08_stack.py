"""
    组合stack  split分离
"""
import numpy as np
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
print(a)
print(b)
c = np.hstack((a,b))
print(c)
a,b,= np.hsplit(c,2)
print(a)
print(b)

c = np.vstack((a,b))
print(c)
a,b = np.vsplit(c,2)
print(a)
print(b)