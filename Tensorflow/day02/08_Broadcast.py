"""

"""
import tensorflow as tf
a = tf.ones([4,1,1,1])
b = tf.broadcast_to(a,[4,32,32,8])
print(b.shape)
#tile()对应维度相乘
c = tf.tile(a,[2,2,2,2])
print(c)