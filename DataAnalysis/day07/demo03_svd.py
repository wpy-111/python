"""
    奇异值分解
"""
import numpy as np
A = np.mat('2 6 8;3 5 11')
#U，V是正交矩阵  U*U.T = E
U,S,V = np.linalg.svd(A,full_matrices=False)
print(U)
print(U*U.T)
print(V)
print(V*V.T)
print(S)
#通过U，S，V 计算原矩阵
A2 = U*np.diag(S)*V
print(A2)