"""
    索引
"""
import tensorflow as tf
a = tf.ones((2,3,5))
print(a)
print('=============================================')
#每一个【】代表一个维度从高纬度开始
print(a[1][0])
#通用索引
print(a[0,1])