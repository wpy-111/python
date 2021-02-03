"""
    填充
"""
import tensorflow as tf
#fill()第一个参数是shape，第二个参数是值
a = tf.fill((3,3),5)
print(a)