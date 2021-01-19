"""
    范围缩放
"""
import sklearn.preprocessing as sp
import numpy as np
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
r = sp.scale(raw_samples)
#缩放器 损失了数据意义
mms = sp.MinMaxScaler(feature_range=(0,1))
r = mms.fit_transform(raw_samples)
print(r)
data = []
# 手动操作对原数组每列做缩放操作
for col_index in range(raw_samples.shape[1]):
    col_val = raw_samples[:,col_index] #拿出二维数组的每一列
    A = np.array([[col_val.min(),1],[col_val.max(),1]])
    B = np.array([0,1])
    x = np.linalg.lstsq(A,B)[0]
    col = col_val * x[0] +x[1]
    data.append(col)
print(np.array(data).T)

