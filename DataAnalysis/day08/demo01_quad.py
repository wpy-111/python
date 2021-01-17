"""
    积分模块
"""
import numpy as np
import scipy.integrate as si
def f(x):
    return 2 * x ** 2 + 3 * x + 4

a,b = -5,5
#r是一个元组，第一个是积分值，第二个是误差值
r = si.quad(f,a,b)[0]
print(r)
#微元法求积分
n = 1000
xs = np.linspace(a,b,n+1)
ys = f(xs)
area = 0
#求每一个小梯行的面积之和
for i in range(n):
    area += (ys[i]+ys[i+1])*(xs[i+1]-xs[i])/2
print(area)





