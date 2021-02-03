"""
    创建tensor
"""
import tensorflow as tf
import numpy as np
#convert_tp_tensor()参数可以是naddary或者列表都可以
a = tf.convert_to_tensor(np.ones([2,3]),dtype=tf.int32)
print(a)
b = tf.convert_to_tensor([1,5,6],dtype=tf.int32)
print(b)