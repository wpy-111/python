"""
    独热编码 OneHOtEncoder()  不能使用连续数据
"""
import numpy as np
import sklearn.preprocessing as sp
samples= np.array([[1,3,2],[7,5,4],[1,8,6],[7,3,9]])
print(samples)
#spare=True 结果是稀疏矩阵  稀疏矩阵变nddary r.toarray()
ohe = sp.OneHotEncoder(sparse=False)
r = ohe.fit_transform(samples)
print(r)