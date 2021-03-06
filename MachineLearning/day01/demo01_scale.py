"""
    均值移除  r 的值 （原数据-均值）/标准差
"""
import sklearn.preprocessing as sp
import numpy as np
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
r = sp.scale(raw_samples)
print(r)
print(np.mean(r, axis=0))
print(np.std(r, axis=0))
