"""
    二值化
"""
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
#设置阈值  小于等于80的值都归0
bin = sp.Binarizer(threshold=80)
r = bin.transform(raw_samples)
print(r)


