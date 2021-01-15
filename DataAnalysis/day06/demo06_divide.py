"""
    除法与取整
"""
import numpy as np
# np.floor(a / b)		# （真除的结果向下取整）
# np.ceil(a / b) 		# （真除的结果向上取整）
# np.trunc(a / b)		# （真除的结果截断取整）
# np.round(a / b)		# （真除的结果四舍五入取整）
a = np.array([10, 20, -30])
b = np.array([3, -3, 6])

# 真除
c = np.divide(a, b)  # c = a / b
print('array:', c)

# 对ndarray做floor操作
d = np.floor(a / b)
print('floor_divide:', d)

# 对ndarray做ceil操作
e = np.ceil(a / b)
print('ceil ndarray:', e)

# 对ndarray做trunc操作
f = np.trunc(a / b)
print('trunc ndarray:', f)

# 对ndarray做around四舍五入操作
g = np.around(a / b)
print('around ndarray:', g)