"""
    维度变化
"""
import tensorflow as tf
a = tf.random.uniform([4,28,28,3])
b = tf.reshape(a,[4,784,3])
#-1自适应
c = tf.reshape(a,[4,-1,3])
