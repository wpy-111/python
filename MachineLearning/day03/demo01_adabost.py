"""
    波士顿地区房屋价格 adaboost 正向激励
"""

import numpy as np
import sklearn.tree as st
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.metrics as sm
import matplotlib.pyplot as mp
# 加载波士顿地区房价数据集
boston = sd.load_boston()
# print(boston.data.shape) #输入集
# print(boston.target.shape) #输出集
# print(boston.feature_names) #特征名称
# # print(boston.data)
# print(boston.target)
#1.打乱数据集  random_state:若两次shuffle使用的随机种子值相同，随机得到的结果也相同
x,y = su.shuffle(boston.data,boston.target,random_state=7)
#2.拆分测试集与训练集，拿总样本的80%做训练，拿20%做测试
train_size = int(len(x)*0.8)
train_x,train_y,test_x,test_y = x[:train_size],y[:train_size],x[train_size:],y[train_size:]
#3.使用训练集训练决策树模型
model = st.DecisionTreeRegressor(max_depth=5)
model.fit(train_x,train_y)
#4.使用测试集进行测试
pre_y = model.predict(test_x)
print(sm.r2_score(test_y,pre_y))

#获取特征重要性
fi = model.feature_importances_
# mp.figure('DT tree',facecolor='lightgrey')
mp.subplot(121)
mp.title('DT tree',fontsize=16)
mp.grid(linestyle=':')
mp.xlabel('feature')
mp.ylabel('FI')
sort_index = np.argsort(fi)[::-1]
x = np.arange(boston.feature_names.size)
mp.bar(x,fi[sort_index],color='dodgerblue',label='DT feature importance')
mp.xticks(x,boston.feature_names[sort_index])
mp.tight_layout()
mp.legend()

import sklearn.ensemble as se
#基于正向激励训练模型 Adaboost模型
model = se.AdaBoostRegressor(model,n_estimators=400,random_state=7)
model.fit(train_x,train_y)
print(model.feature_importances_)
pre_boost_y = model.predict(test_x)
print(sm.r2_score(test_y,pre_boost_y))
fi = model.feature_importances_
mp.subplot(122)
# mp.figure('Adaboost FI',facecolor='lightgrey')
mp.title('Adaboost FI',fontsize=16)
mp.grid(linestyle=':')
mp.xlabel('feature')
mp.ylabel('FI')
sort_index = np.argsort(fi)[::-1]
x = np.arange(boston.feature_names.size)
mp.bar(x,fi[sort_index],color='orangered',label='Adaboost feature importance')
mp.xticks(x,boston.feature_names[sort_index])
mp.tight_layout()
mp.legend()
mp.show()