"""
    轮廓系数 [-1,1]
    import sklearn.metrics as sm
    v：平均轮廓系数
    metric：距离算法：使用欧几里得距离(euclidean)
    v = sm.silhouette_score(输入集, 输出集, sample_size=样本数, metric=距离算法)
"""
import sklearn.metrics as sm
import sklearn.cluster as sc
import numpy as np
import matplotlib.pyplot as mp
data = np.loadtxt('multiple3.txt',delimiter=',')
#k均值
model = sc.KMeans(n_clusters=4)
model.fit(data)
data_y = model.labels_
centers = model.cluster_centers_
print(centers)
#计算轮廓系数
coef = sm.silhouette_score(data,data_y,sample_size=len(data),metric='euclidean')
print(coef)



l, r = data[:, 0].min() - 1, data[:, 0].max() + 1
b, t = data[:, 1].min() - 1, data[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(samples)
grid_z = grid_z.reshape(grid_x.shape)
mp.figure('K Means',facecolor='lightgrey')
mp.title('K Means',fontsize=16)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(data[:,0],data[:,1],c=data_y,cmap='brg',s=80,label='Samples')
mp.scatter(centers[:,0],centers[:,1],s=300,marker='+',label='Centers',color='yellow')
mp.legend()
mp.tight_layout()
mp.show()
