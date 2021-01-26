"""
    学习曲线
    import sklearn.model_selection as ms
    _，train_score,test_score = ms.learning_curve(model,train_x,train_y,[0.9,0.8,0.7],cv=5)
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.metrics as sm
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp
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
#学习曲线，得到最优的训练集大小
pararm =np.arange(0.1,1,0.1)
_,train_score,test_score = ms.learning_curve(model,train_x,train_y,train_sizes=pararm,cv=5)
score = test_score.mean(axis=1)
mp.figure('Learing Curve',facecolor='lightgray')
mp.title('learning Curve',fontsize=16)
mp.xlabel('train_size',fontsize=14)
mp.ylabel('f1_weighted',fontsize=14)
mp.grid(':')
mp.plot(np.arange(0.1,1,0.1),score,'o-',color='dodgerblue',label='LC')
mp.legend()
mp.tight_layout()
mp.show()
