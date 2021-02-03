"""
    tensor变量
"""
import tensorflow as tf
import numpy as np
a = tf.range(5)
print(a)
b = tf.Variable(a)
print(b)
c = tf.Variable(a,name='input_data')#name 参数中不能由空格
print(c)
