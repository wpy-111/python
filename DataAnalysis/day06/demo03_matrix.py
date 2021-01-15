"""
    矩阵
"""
import numpy as np
# ary = np.array([[1,2,3],[4,5,6]])
# m = np.matrix(ary,copy=True)
# print(ary,type(ary))
# print(m,type(m))
# m1 = np.mat('1 2 3 4;5 6 7 8')
# print(m1,type(m1))
# m2 = np.mat(ary)
# print(m2,type(m2))
#矩阵乘法
ary = np.arange(1,10).reshape(3,3)
print(ary)
print(ary * ary)

m = np.mat(ary)
print(m)
print(m * m)
#矩阵的逆
ary = np.mat('1 4 5;3 6 7;5 8 11')
print(ary)
print(ary.T)#转置
print(ary.I)#逆矩阵
print(ary * ary.I)

# 解方程
A = np.mat('3 3.2;3.5 3.6')
B = np.mat('118.4;135.2')
#最小二乘法求拟合  x 是拟合值
x = np.linalg.lstsq(A,B)[0]
print(x)
#解方程  x 是精确值
x = np.linalg.solve(A,B)
print(x)