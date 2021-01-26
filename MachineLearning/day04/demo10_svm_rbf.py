"""
    支持向量积 径向基核函数
    model = svm.SVC(kernel='rbf')
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.model_selection as ms
import sklearn.svm as svm
data = np.loadtxt('../data/multiple2.txt', unpack=False, dtype='U20', delimiter=',')
print(data.shape)
x = np.array(data[:, :-1], dtype=float)
y = np.array(data[:, -1], dtype=float)
train_x,test_x,train_y,test_y = ms.train_test_split(x,y,test_size=0.25,random_state=7)
#创建svm模型
model = svm.SVC(kernel='rbf',C=600,gamma=0.01)
model.fit(train_x,train_y)
pre_y = model.predict(test_x)
print((pre_y==test_y).sum()/test_y.size)#精确度
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(samples)
grid_z = grid_z.reshape(grid_x.shape)

mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()

