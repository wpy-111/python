"""
    掩码
"""
import tensorflow as tf
a = tf.ones([4,28,28,3])
print(a)
b = tf.boolean_mask(a,mask=[True,False,False,True],axis=0)
print(b.shape)