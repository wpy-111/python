"""
    索引
"""
import tensorflow as tf
a = tf.ones([4,35,8])
print(a)
#axis是按照第几个维度  只能对一个维度进行操作
b = tf.gather(a,axis=0,indices=[1,2])
print(b)
print('============================')
#gather_nd()可以同时对多个维度进行操作
c = tf.gather_nd(a,[0,1])
print(c.shape)
#双括号返回的是数组
d = tf.gather_nd(a,[[0,1]])
print(d.shape)


