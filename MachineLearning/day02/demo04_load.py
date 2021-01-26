"""
    加载模型
    import pickle
    model = pickle.load(f)
"""
import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
data = np.loadtxt('./single.txt',delimiter=',',usecols=(0,1),unpack=False)
#x 必须是二维数组，y必须是一维数组  一行一样本 一列一特征
x = data[:,0].reshape(-1,1)
y = data[:,1]
#加载模型
import pickle
with open('linear.pkl','rb') as f :
    model = pickle.load(f)
pre_y = model.predict(x)
mp.figure('Linear Regression',facecolor='lightgrey')
mp.title('Linear Regression',fontsize=16)
mp.grid(linestyle=':')
mp.scatter(data[:,0],data[:,1],color='dodgerblue',label='Samples',s=80)
mp.plot(x,pre_y,color='orangered',label='pre_line')
mp.legend()
mp.show()

#评估训练模型误差
import sklearn.metrics as sm
print(sm.mean_absolute_error(y,pre_y))
print(sm.mean_squared_error(y,pre_y))
print(sm.median_absolute_error(y,pre_y))
#评分越接近1误差越小
print(sm.r2_score(y,pre_y))








