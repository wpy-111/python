"""
    均值漂移
    # 量化带宽，决定每次调整概率密度函数的步进量
    # n_samples：样本数量
    # quantile：量化宽度（直方图一条的宽度）
    bw = sc.estimate_bandwidth(x, n_samples=len(x), quantile=0.1)
    # 均值漂移聚类器
    model = sc.MeanShift(bandwidth=bw, bin_seeding=True)
    model.fit(x)
"""
import sklearn.metrics as sm
import sklearn.cluster as sc
import numpy as np
import matplotlib.pyplot as mp
data = np.loadtxt('multiple3.txt',delimiter=',')
bw = sc.estimate_bandwidth(data,n_samples=len(data),quantile=0.1)
#漂移均值
model = sc.MeanShift(bandwidth=bw,bin_seeding=True)
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
mp.figure('Mean Shift',facecolor='lightgrey')
mp.title('Mean Shift',fontsize=16)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(data[:,0],data[:,1],c=data_y,cmap='brg',s=80,label='Samples')
mp.scatter(centers[:,0],centers[:,1],s=300,marker='+',label='Centers',color='yellow')
mp.legend()
mp.tight_layout()
mp.show()
