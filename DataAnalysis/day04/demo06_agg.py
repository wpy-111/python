"""
    轴向汇总
"""
import numpy as np
data = np.array([[88,88,88,88],
                 [99,88,68,77],
                 [99,85,77,98]])
print(data)
# 轴向汇总
def func(data):

    return np.mean(data),np.max(data),np.min(data)
result = np.apply_along_axis(func,0,data)
print(result)


