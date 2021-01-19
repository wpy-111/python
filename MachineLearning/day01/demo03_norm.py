"""
    归一化 对行
"""
import numpy as np
import sklearn.preprocessing as sp
samples = np.array([[20.,10.,5.],[4.,2.,1.],[18.,11.,12.]])
#normalize(norm=l2)默认l2
#    l1 - l1范数，向量中个元素绝对值之和
#    l2 - l2范数，向量中个元素平方之和
r = sp.normalize(samples,norm='l1')
print(r)
print(r.sum(axis=1))