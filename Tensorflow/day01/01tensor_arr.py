import tensorflow as tf
print(tf.constant(1.0))
print(tf.constant(1))
print(tf.constant('hello world'))
print(tf.constant([True,False]))
print(tf.constant([[2,5],[5,6]]))
a = tf.constant([1,5,6,8])
print(a.device)#返回设备的名字
#创建环境
with tf.device('cpu'):
    b = tf.constant([[5,6,8,52,6],[5,8,5,54,5]])
    print(b.shape)#返回tensor的（2，5）
    print(b.ndim)#返回tensor的维度
with tf.device('gpu'):
    c = tf.constant(1.0)
    print(c.ndim)  # 返回tensor的维度 0 scale
print(c.device)#返回设备的名字
print(b.gpu().device)
print(a.numpy)#将tensor转化为一个nddary