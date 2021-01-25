"""
    分类报告 sm.classificantion_report(test_y,pre_y)
"""
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp
import sklearn.model_selection as ms
data = np.loadtxt('../data/multiple1.txt', unpack=False, dtype='U20', delimiter=',')
print(data.shape)
x = np.array(data[:, :-1], dtype=float)
y = np.array(data[:, -1], dtype=float)
train_x,test_x,train_y,test_y = ms.train_test_split(x,y,test_size=0.25,random_state=7)
# 创建高斯分布朴素贝叶斯分类器
model = nb.GaussianNB()
model.fit(train_x, train_y)
#针对测试样本进行测试，看一下每一测试样本的预测输出
pre_y = model.predict(test_x)
print((pre_y==test_y).sum()/test_y.size)#精确度
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(samples)
grid_z = grid_z.reshape(grid_x.shape)
#输出混淆矩阵
import sklearn.metrics as sm
m = sm.confusion_matrix(test_y,pre_y)
#输出分类报告
cr = sm.classification_report(test_y,pre_y)

mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()
