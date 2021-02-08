"""
    上采样的方法
"""
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph
import numpy as np
import paddle.nn.functional as F
def main():
    with dygraph.guard(fluid.CUDAPlace(0)):
        data = np.array([[1,2],
                         [3,4]]).astype('float32')

        # data = np.arange(1,10).astype('float32')
        data = data[np.newaxis,np.newaxis,:,:]
        data = dygraph.to_variable(data)
        # out = fluid.layers.interpolate(data,out_shape=(4,4),align_corners=True)paddle1.8
        out = F.interpolate(data,size=(4,4),align_corners=True,mode='bilinear')
        # [[[[1.        1.3333333 1.6666667 2.]
        #    [1.6666666 2.        2.3333335 2.6666665]
        #   [2.3333333 2.6666667 3.0000002 3.3333335]
         # [3.        3.3333333 3.6666667 4.]]]]

        print(out)

if __name__ == '__main__':
    main()





