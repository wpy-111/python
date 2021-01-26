"""
    交通流量预测(回归)
    1.判断模型是回归还是分类
    2.整理样本数据，做特征分析（1.离散型，连续性2.特征数值分布）完成样本预处理（特征工程）
    3.整理输入集输出集，做模型选择（拆分训练测试集，交叉验证，验证曲线，学习曲线，网格搜索）
    4.训练模型，使用测试数据测试，调参
    5.应用
"""
import sklearn.preprocessing as sp
import numpy as np
import sklearn.model_selection as ms
import sklearn.metrics as sm
import sklearn.ensemble as se
import sklearn.utils as su
data = np.loadtxt('traffic.txt',delimiter=',',dtype='U20')
x = data[:,:-1]
y = data[:,-1].astype('int32')
x,y = su.shuffle(x,y,random_state=7)
train_size = int(len(x)*0.75)
x,test_x,train_y,test_y = x[:train_size],x[train_size:],y[:train_size],y[train_size:]
encoders = []
train_x = []
for col_ind in range(x.shape[1]):
    col_val = x[:,col_ind]
    encoder = sp.LabelEncoder()
    encoders.append(encoder)
    train_x.append(encoder.fit_transform(col_val))
train_x = np.array(train_x).T
model = se.RandomForestRegressor(max_depth=10,min_samples_split=2,n_estimators=500)
model.fit(train_x,train_y)
test1_x = []
for col_ind in range(x.shape[1]):
    col_val = test_x[:,col_ind]
    test1_x.append(encoders[col_ind].transform(col_val))
test1_x = np.array(test1_x).T
pre_y = model.predict(test1_x)
print(sm.r2_score(test_y,pre_y))





