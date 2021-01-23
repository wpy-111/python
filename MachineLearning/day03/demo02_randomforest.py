"""
    随机森林   sklearn.ensemble    分析共享单车投放
"""
import sklearn.ensemble as se
import pandas as pd
import sklearn.utils as su
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import numpy as np
data = pd.read_csv('bike_day.csv',sep=',')
data = data.drop(['instant','dteday','casual','registered'],axis=1)
#整理样本输入集和输出集
#打乱数据集 拆分测试集和训练集 90%
x,y = data[data.columns[:-1]],data['cnt']
x,y = su.shuffle(x,y,random_state=7)
size = int(len(x)*0.9)
train_x,train_y,test_x,test_y = x[:size],y[:size],x[size:],y[size:]
#训练模型
model = se.RandomForestRegressor(n_estimators=1000,max_depth=10,min_samples_split=2)
model.fit(train_x,train_y)
pre_y = model.predict(test_x)
print(sm.r2_score(test_y,pre_y))
print(sm.mean_absolute_error(test_y,pre_y))
#输出特征重要性
fi = model.feature_importances_
mp.figure('RF fi',facecolor='lightgrey')
mp.title('RF fi ',fontsize=16)
mp.grid(linestyle=':')
mp.xlabel('feature')
mp.ylabel('FI')
sort_index = np.argsort(fi)[::-1]
x_1 = np.arange(x.columns.size)
mp.bar(x_1,fi[sort_index],color='orangered',label='Random Forest Fi')
mp.xticks(x_1,x.columns[sort_index])
mp.tight_layout()
mp.legend()
mp.show()
