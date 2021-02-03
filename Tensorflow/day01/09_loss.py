import tensorflow as tf
out = tf.random.uniform([4,10])
print(out)
y =tf.constant([2,1,3,4])
print(y)
#参数第一个是编码为1的序列，depth是有多少列
c = tf.one_hot(y,depth=5)
print(c)
print(tf.__version__)