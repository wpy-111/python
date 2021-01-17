"""
    插值
"""
# 插值操作示例
import numpy as np
import matplotlib.pyplot as mp
import scipy.interpolate as si

# 生成一组散点
min_x = -50
max_x = 50
x = np.linspace(min_x, max_x, 15)
y = np.sinc(x)

mp.scatter(x, y, s=60, color="dodgerblue", marker="o", label="Samples")
# 通过样本点生成插值器函数
linear = si.interp1d(x, y, kind="linear")
linear_x = np.linspace(min_x, max_x, 1000)  # 产生一组新的点
linear_y = linear(linear_x)  # 计算y值
mp.plot(linear_x, linear_y, color="green", label="linear interplt")

# 三次样条插值 （CUbic Spline Interpolation） 获得一条光滑曲线
cubic = si.interp1d(x, y, kind='cubic')
cub_x = np.linspace(min_x, max_x, 200)
cub_y = cubic(cub_x)
mp.plot(cub_x, cub_y, color="orangered", linestyle=":",
        linewidth=4, alpha=0.8, label="linear interplt")

mp.grid()
mp.legend()
mp.show()