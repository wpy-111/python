"""
    事件预测
"""
import sklearn.preprocessing as sp
import numpy as np
import sklearn.model_selection as ms
import sklearn.metrics as sm
import sklearn.svm as svm
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

#3.测试