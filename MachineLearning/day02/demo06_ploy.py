"""
    多项式回归
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.pipeline as pl
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
data = np.loadtxt('./single.txt',delimiter=',',usecols=(0,1),unpack=False)
model = lm.LinearRegression()
#x 必须是二维数组，y必须是一维数组  一行一样本 一列一特征
x = data[:,0].reshape(-1,1)
y = data[:,1]
test_x = np.linspace(np.min(x),np.max(x),200).reshape(-1,1)
model.fit(x,y)
pre_y = model.predict(test_x)
# 基于数据训练多项式回归模型  10次数
model = pl.make_pipeline(sp.PolynomialFeatures(10),lm.LinearRegression())
model.fit(x,y)
#绘制多项式曲线
pre_ploy_y = model.predict(test_x)

mp.figure('Linear Regression',facecolor='lightgrey')
mp.title('Linear Regression',fontsize=16)
mp.grid(linestyle=':')
mp.scatter(data[:,0],data[:,1],color='dodgerblue',label='Samples',s=80)
mp.plot(test_x,pre_y,color='orangered',label='pre_line')
mp.plot(test_x,pre_ploy_y,color='red',label='ploy_y')
mp.legend()
mp.show()