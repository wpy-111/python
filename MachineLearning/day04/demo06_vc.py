"""
    验证曲线
    import sklearn.model_selection as ms
    train_score,test_score = ms.validation_curve(model,train_x,train_y,'n_estimators',np.arange(50,550,50),cv=5)
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.metrics as sm
import sklearn.ensemble as se
import sklearn.model_selection as ms
import pickle
import matplotlib.pyplot as mp
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
model = se.RandomForestClassifier(n_estimators=100,max_depth=12,min_samples_split=2,random_state=7)
#验证曲线 得到最优的参数
train_score1,test_score1 = ms.validation_curve(model,train_x,train_y,'n_estimators',np.arange(50,550,50),cv=5)
score1 = test_score1.mean(axis=1)
train_score2,test_score2 = ms.validation_curve(model,train_x,train_y,'max_depth',np.arange(5,16),cv=5)
score2 = test_score2.mean(axis=1)
mp.figure('Validation Curve',facecolor='lightgray')
mp.subplot(121)
mp.title('Validation Curve',fontsize=16)
mp.xlabel('n_estimators',fontsize=14)
mp.ylabel('f1_weighted',fontsize=14)
mp.grid(':')
mp.plot(np.arange(50,550,50),score1,'o-',color='dodgerblue',label='VC')
mp.legend()
mp.tight_layout()
mp.subplot(122)
mp.title('Validation Curve',fontsize=16)
mp.xlabel('max_depth',fontsize=14)
mp.ylabel('f1_weighted',fontsize=14)
mp.grid(':')
mp.plot(np.arange(5,16),score2,'o-',color='dodgerblue',label='VC')
mp.legend()
mp.tight_layout()
mp.show()
