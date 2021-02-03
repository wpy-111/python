"""
    tensor random 随机数字
"""
import tensorflow as tf
import numpy as np
#正态分布 random.normal()第一个参数是shape，第二个参数mean均值，第三个参数stddv标准差
a = tf.random.normal([3,3],mean=10,stddev=0.1)
print(a)
#截断的正态分布 当值大于某一个固定的值截断
# 第一个参数是shape，第二个参数mean均值，第三个参数stddv标准差
b = tf.random.truncated_normal([3,3],mean=10,stddev=0.1)
print(b)
#均匀分布 第一个参数shape，第二个参数从哪开始minval，第三个参数结束位置maxval
c = tf.random.uniform([5,5],minval=0,maxval=10,dtype=tf.int32)
print(c)