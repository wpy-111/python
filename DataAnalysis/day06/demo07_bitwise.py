"""
    位运算
"""
import numpy as np
a = np.array([0, -1, 2, -3, 4, -5])
b = np.array([0, 1, 2, 3, 4, 5])
#^位异或操作符  相同得0 不同得1
print(a^b)