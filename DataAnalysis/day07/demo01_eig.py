"""
    特征向量
"""
import numpy as np

A = np.mat('1 4 5 ;2 6 8;3 5 8')
print(A)
#提取特征值
eigvals,eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
#通过特征值和特征向量计算原矩阵
#np.diag()将数组对角化
B = eigvecs * np.diag(eigvals) * eigvecs.I
print(B)


