"""
    波士顿地区房屋价格
"""
import numpy as np
import sklearn.tree as st
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.metrics as sm
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