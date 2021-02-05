"""
    数据集加载
"""
import tensorflow as tf
from tensorflow.keras import datasets

def prepare_mnist(x,y):
    x = tf.cast(x,tf.int32)
    y = tf.cast(y,tf.float32)
    return x,y

(train_x,train_y),(test_x,test_y) = datasets.fashion_mnist.load_data()
train_y = tf.one_hot(train_y,depth=10)
test_y = tf.one_hot(test_y,depth=10)
#转化到一个数据集
ds = tf.data.Dataset.from_tensor_slices((train_x,train_y))
print(ds)




