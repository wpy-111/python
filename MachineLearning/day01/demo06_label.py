"""
    标签编码 获取一组数据，针对这组字符串数据完成标签编码，输出结果
"""
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array(['audi', 'ford', 'audi', 'toyota','ford', 'bmw', 'toyota', 'ford','audi'])
#创建标签编码器
lbe = sp.LabelEncoder()
r =lbe.fit_transform(raw_samples)
print(r)
#反解码
r = lbe.inverse_transform(r)
print(r)
