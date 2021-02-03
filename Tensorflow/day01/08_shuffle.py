"""
    随机打散
"""
import tensorflow as tf
a = tf.range(10)
print(a)
b = tf.random.shuffle(a)
print(b)
d = tf.constant([1,2,3,4,5,6,7,8,9])
#gather第一个参数tensor，第二个参数序列索引
c = tf.gather(d,b)
print(c)