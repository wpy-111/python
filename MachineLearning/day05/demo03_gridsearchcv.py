"""
    网格搜索
    import sklearn.model_selection as sm
    model = sm.GridSearchCV(model,[{},{}],cv=5)
    调取得到的参数
    # 获取网格搜索每个参数组合
    model.cv_results_['params']
    # 获取网格搜索每个参数组合所对应的平均测试分值
    model.cv_results_['mean_test_score']
    # 获取最好的参数
    model.best_params_
    model.best_score_
    model.best_estimator_
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.model_selection as sm
data = np.loadtxt('multiple2.txt', unpack=False, dtype='U20', delimiter=',')
print(data.shape)
x = np.array(data[:, :-1], dtype=float)
y = np.array(data[:, -1], dtype=float)
train_x,test_x,train_y,test_y = ms.train_test_split(x,y,test_size=0.25,random_state=7)
#创建svm模型
model = svm.SVC(kernel='rbf',C=600,gamma=0.01,probability=True)
params = [{'kernel':['linear'], 'C':[1, 10, 100, 1000]},
    {'kernel':['poly'], 'C':[1], 'degree':[2, 3]},
    {'kernel':['rbf'], 'C':[1,10,100,1000], 'gamma':np.arange(0.1,1,0.1)}]
model = ms.GridSearchCV(model,params,cv=5)
model.fit(train_x,train_y)
#训练之后，获取模型最优参数
print(model.best_params_)
print(model.best_score_)
print(model.best_estimator_)
#zip打包   获取每组参数的数值和得分
for p,s in zip(model.cv_results_['params'],model.cv_results_['mean_test_score']):
    print(p,s)

pre_y = model.predict(test_x)
print((pre_y==test_y).sum()/test_y.size)#精确度
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(samples)
grid_z = grid_z.reshape(grid_x.shape)
mp.figure('GS CV', facecolor='lightgray')
mp.title('GS CV', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
#新增样本，输出新增样本的置信概率
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
pre_y = model.predict(prob_x)
probs = model.predict_proba(prob_x)
print(pre_y)
print(probs)
mp.legend()
mp.show()


