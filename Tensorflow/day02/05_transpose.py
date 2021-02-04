"""
    transpose 相当于转置
"""
import tensorflow as tf
a = tf.random.normal([4,3,2,1])
print(a)
#默认是维度倒叙排一次
b = tf.transpose(a)
print(b.shape)
c = tf.transpose(b,perm=[0,2,1,3])
print(c.shape)