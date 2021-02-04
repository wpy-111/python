"""
    前向传播
"""
import tensorflow as tf
from tensorflow.keras import datasets
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#加载数据  x = [60k,28,28]
# y = [60k]
(x,y) ,_= datasets.mnist.load_data()
#转化tensor
x = tf.convert_to_tensor(x,dtype=tf.float32)/255.
y = tf.convert_to_tensor(y,dtype=tf.int32)
print(tf.reduce_min(x),tf.reduce_max(x))
print(tf.reduce_min(y),tf.reduce_max(y))
train_db = tf.data.Dataset.from_tensor_slices((x,y)).batch(128)
train_iter = iter(train_db)
sample = next(train_iter)








