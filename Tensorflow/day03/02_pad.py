"""
    数据填充
"""
import tensorflow as tf
a = tf.reshape(tf.range(9),[3,3])
print(a)
#padding[[对行的填充]，[对列的填充]]
b = tf.pad(a,paddings=[[1,1],[0,1]])
print(b)