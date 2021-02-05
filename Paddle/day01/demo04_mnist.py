"""
    手写数字的识别 minst
"""
import paddle
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph
import cv2 as cv
import numpy as np
train_reader = paddle.batch(paddle.dataset.mnist.train(),batch_size=8)
for batch_id,data in enumerate(train_reader()):
    img_data = np.array([x[0] for x in data]).astype('float32')
    label_data = np.array([x[1] for x in data]).astype('float32')
    print(img_data.shape,img_data[0])
    print(label_data.shape,label_data)
    img = np.array(img_data[0]+1)*127.5
    img = img.reshape(28,28)
    cv.imshow('img',img)
    cv.waitKey()
    break