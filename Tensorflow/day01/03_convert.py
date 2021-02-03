"""
    tensor类型相互转化 tf.cast()
"""
import tensorflow as tf
import  numpy  as np
a = np.array([0,1,2,3,4])
print(a.dtype)
aa = tf.convert_to_tensor(a)
print(aa)
aa = tf.convert_to_tensor(a,dtype=tf.int64)
print(aa)
aaa = tf.cast(aa,dtype=tf.float32)
bbb = tf.cast(aa,dtype=tf.bool)
print(aaa)
print(bbb)
#将tensor转化为numpy
print(aaa.numpy())