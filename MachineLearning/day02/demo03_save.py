"""
    保存模型
    import pickle
    pickle.dump(model,f)
"""
import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as mp
import  numpy as np
data = np.loadtxt('./single.txt',delimiter=',',usecols=(0,1),unpack=False)
model = lm.LinearRegression()
#x 必须是二维数组，y必须是一维数组  一行一样本 一列一特征
x = data[:,0].reshape(-1,1)
y = data[:,1]
model.fit(x,y)
#保存模型
import pickle
with open('linear.pkl','wb') as f:
    pickle.dump(model,f)
print('save success....')








