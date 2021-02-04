"""
    合并
"""
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
a = tf.ones([4,35,8])
b = tf.ones([4,35,8])
#需要拼接的维度必循相同
c = tf.concat([a,b],axis=0)
print(c)
#创建一个新的维度  两组数据维度必须相同
d = tf.stack([a,b],axis=0)
print(d.shape)
e = tf.ones([2,3,4,2])
f,b = tf.unstack(e,axis=-1)
print(f.shape,b.shape)
#split灵活性强 ，可以指定分开数量
n,m = tf.split(e,axis=-2,num_or_size_splits=2)
print(n.shape,m.shape)