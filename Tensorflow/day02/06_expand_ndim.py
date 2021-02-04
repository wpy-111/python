"""
    增加维度
"""
import tensorflow as tf
a = tf.random.normal([4,35,8])
b = tf.expand_dims(a,axis=0)
print(b.shape)
c = tf.expand_dims(a,axis=3)
print(c.shape)
#  -1是往最后一个地方增加维度
d = tf.expand_dims(a,axis=-1)
print(d.shape)