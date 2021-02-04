"""
    数学运算
"""
import tensorflow as tf
#平方 pow()方法或者 **
a = tf.fill((2,2),2)
b = tf.pow(a,3)
print(b)
print(a*b)#对应位置相乘
print(a@b)#矩阵乘法运算
print(tf.matmul(a,b))#矩阵乘法运算