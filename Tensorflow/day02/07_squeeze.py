"""
    减少一个维度
"""
import tensorflow as tf
a = tf.zeros([1,2,1,1,3])
b = tf.squeeze(a,axis=0)
print(b.shape)