"""
    分类 se.RandomForestClassifier()大概流程
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.metrics as sm
import sklearn.ensemble as se
import sklearn.model_selection as ms
import pickle
#加载数据，针对每一列做标签编码，构建纯数字的数据集   unpack是否拆包
data = np.loadtxt('./car.txt',delimiter=',',unpack=False,dtype='U10')
x = data[:,:-1]
y = data[:,-1]
#针对每一列做标签编码  sp.LabelEncoder().fit_transform(一维数组)
train_x = []
encoders = []
for col_index in range(x.shape[1]):
    col_val = x[:,col_index]
    label_encoder = sp.LabelEncoder()
    encoders.append(label_encoder)
    encoder_col = label_encoder.fit_transform(col_val)
    train_x.append(encoder_col)
train_x = np.array(train_x).T
yencoder = sp.LabelEncoder()
train_y = yencoder.fit_transform(y)
#针对样本做一次交叉验证 ，看一下得分  深度和列差不多
model = se.RandomForestClassifier(n_estimators=140,max_depth=9,min_samples_split=2,random_state=7)
score = ms.cross_val_score(model,train_x,train_y,cv=5,scoring='f1_weighted')
print(score.mean())
#训练随机森林分类器模型
model.fit(train_x,train_y)
with open('car_model.pkl','wb') as f:
    pickle.dump(model,f)
pre_y = model.predict(train_x)
print((pre_y==train_y).sum()/train_y.size)
#针对测试集进行测试   商用
data = [
    ['high', 'med', '5more', '4', 'big', 'low', 'unacc'],
    ['high', 'high', '4', '4', 'med', 'med', 'acc'],
    ['low', 'low', '2', '4', 'small', 'high', 'good'],
    ['low', 'med', '3', '4', 'med', 'high', 'vgood']]
data_y = np.array(data)[:,-1]
data = np.array(data)[:,:6]
test_x = []
for col_ind in range(data.shape[1]):
    col_val = data[:,col_ind]
    encoder_col = encoders[col_ind].transform(col_val)
    test_x.append(encoder_col)
test_x = np.array(test_x).T
pre_test_y = model.predict(test_x)
print(yencoder.inverse_transform(pre_test_y))
y = yencoder.transform(data_y)
print(sm.classification_report(y,pre_test_y))