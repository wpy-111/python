"""
    随机森林  分析共享单车投放
"""
import sklearn.ensemble as se
import sklearn.preprocessing as sp
import numpy as np
import pandas as pd
import sklearn.utils as su
import sklearn.metrics as sm
data = pd.read_csv('bike_day.csv',sep=',')
data = data.drop(['instant','dteday','casual','registered'],axis=1)
#整理样本输入集和输出集
#打乱数据集 拆分测试集和训练集 90%
x,y = data[data.columns[:-1]],data['cnt']
x,y = su.shuffle(x,y,random_state=7)
size = int(len(x)*0.9)
train_x,train_y,test_x,test_y = x[:size],y[:size],x[size:],y[size:]
#训练模型
model = se.RandomForestRegressor(n_estimators=1000,max_depth=5,min_samples_split=2)
model.fit(x,y)
pre_y = model.predict(test_x)
print(sm.r2_score(test_y,pre_y))

