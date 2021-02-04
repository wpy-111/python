"""
    排序
"""
import tensorflow as tf
a = tf.random.shuffle(tf.range(5))
print(a)
b = tf.sort(a,direction='ASCENDING')#升序默认
print(b)
c = tf.sort(a,direction='DESCENDING')#下降
print(c)
d = tf.argsort(a,direction='ASCENDING')
print(d)
print(tf.gather(a,d))