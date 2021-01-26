"""
    事件预测
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
import sklearn.svm as svm
import sklearn.utils as su
class DigitEncoder():
    """数字编码器 """
    def fit_transform(self,y):
        return y.astype(int)
    def transform(self,y):
        return y.astype(int)
    def inverse_transform(self,y):
        return y.astype(str)
#1.加载文件，特征工程，整理输入集和输出集
data = np.loadtxt('event.txt',delimiter=',',dtype='U10')
data = np.delete(data,1,axis=1)
x = data[:,:-1]#输入集
y = data[:,-1]#输出集
encoders = []
train_x =[]
for col_ind in range(x.shape[1]):
    col_val = x[:,col_ind]
    #判断是否是数字字符串
    if col_val[0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    encoders.append(encoder)
    train_x.append(encoder.fit_transform(col_val))
train_x = np.array(train_x).T
yencoder = sp.LabelEncoder()
train_y = yencoder.fit_transform(y)
#2.选择模型并且训练
x,y = su.shuffle(train_x,train_y,random_state=7)
train_x,test_x,train_y,test_y = ms.train_test_split(x,y,test_size=0.25)
model = svm.SVC(kernel='rbf',class_weight='balanced')
score = ms.cross_val_score(model,train_x,train_y,scoring='f1_weighted')
print(score.mean())
# params = [{'kernel':['linear']},
#          {'kernel':['poly'],'degree':[2,3]},
#          {'kernel':['rbf'],'C':[1,100,200,300,500],'gamma':[0.01,0.1,1]}]
# model = ms.GridSearchCV(model,params,cv=5)
model.fit(train_x,train_y)
# for p,s in zip(model.cv_results_['params'],model.cv_results_['mean_test_score']):
#     print(p,s)
pre_test_y = model.predict(test_x)
print(sm.confusion_matrix(test_y,pre_test_y))
print(sm.classification_report(test_y,pre_test_y))
#3.测试
data = [['Tuesday', '13:30:00', '21', '23'],
        ['Sunday', '14:30:00', '2', '2']]
x = np.array(data)
test_x =[]
for col_ind in range(x.shape[1]):
    col_val = x[:,col_ind]
    test_x.append(encoders[col_ind].transform(col_val))
test_x = np.array(test_x).T
pre_test_y = model.predict(test_x)
y = yencoder.inverse_transform(pre_test_y)
print(y)