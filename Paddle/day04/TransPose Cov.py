"""
    反卷积
"""
import paddle
import numpy as np
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph
def main():
    with dygraph.guard(fluid.CUDAPlace(0)):
        data = np.array([[1,2],
                         [3,4]]).astype('float32')

        # data = np.arange(1,10).astype('float32')
        data = data[np.newaxis,np.newaxis,:,:]
        data = dygraph.to_variable(data)
        #====================================================================
        convt = dygraph.Conv2DTranspose(num_channels=1,num_filters=1,filter_size=3)