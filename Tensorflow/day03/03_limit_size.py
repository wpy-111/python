"""
   限幅
"""
import tensorflow as tf
a = tf.range(10)
b = tf.maximum(a,5)#[5 5 5 5 5 5 6 7 8 9]
print(b)
c = tf.minimum(a,5)#[0 1 2 3 4 5 5 5 5 5]
print(c)
d = tf.clip_by_value(a,2,8)
print(d)
