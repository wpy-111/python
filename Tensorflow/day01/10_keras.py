"""
    线性回归模型
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as mp
data = np.loadtxt('single.txt',delimiter=',')
x = data[:,0]
y = data[:,1]
#顺序模型
model = tf.keras.Sequential()
#添加层  第一个参数输出数据的维度， 第二个是输入数据的维度
model.add(tf.keras.layers.Dense(1,input_shape=(1,)))
print(model.summary())
#编译
model.compile(optimizer='adam',loss='mse')
model.fit(x,y,epochs=5000)
y = model.predict(x)
print(y)
mp.figure("learn",facecolor='lightgrey')
mp.title('learn',fontsize=16)
mp.scatter(x,y,s=80,marker='o')
mp.tight_layout()
mp.show()

