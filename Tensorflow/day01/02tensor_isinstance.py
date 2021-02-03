import tensorflow as tf
import numpy as np

a = tf.constant([1.0])
b = tf.constant([True,False])
c = tf.constant('hello world')
d = np.arange(4)
print(d)
print(tf.is_tensor(a))#判断是否为tensor类型
print(tf.is_tensor(d))#判断是否为tensor类型
print(isinstance(a,tf.Tensor))