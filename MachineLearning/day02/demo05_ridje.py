"""
    岭回归 Ridge
    import sklearn.linear_model as lm
    model1 = lm.Ridge(1000,max_iter=10000,fit_intercept=True)
"""
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import  numpy as np
data = np.loadtxt('./abnormal.txt',delimiter=',',usecols=(0,1),unpack=False)
model = lm.LinearRegression()
#x 必须是二维数组，y必须是一维数组  一行一样本 一列一特征
x = data[:,0].reshape(-1,1)
y = data[:,1]
model.fit(x,y)
pre_y = model.predict(x)
#训练岭回归模型，基于当前数据 fit_intercept是否训练截距  max_iter迭代次数
model1 = lm.Ridge(1000,max_iter=10000,fit_intercept=True)
model1.fit(x,y)
ridge_pre_y = model1.predict(x)
mp.figure('Ridge Regression',facecolor='lightgrey')
mp.title('Ridge Regression',fontsize=16)
mp.grid(linestyle=':')
mp.scatter(data[:,0],data[:,1],color='dodgerblue',label='Samples',s=80)
mp.plot(x,pre_y,color='orangered',label='Linear')
mp.plot(x,ridge_pre_y,color='dodgerblue',label='Ridge',alpha=0.5)
mp.tight_layout()
mp.legend()
mp.show()








