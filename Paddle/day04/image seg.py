"""
        图像分割
"""
import paddle
import paddle.fluid as fluid
import numpy as np
from paddle.fluid.dygraph import to_variable
from paddle.nn import Conv2D, MaxPool2D, Linear, Dropout
class BasicModel(fluid.dygraph.Layer):
    def __init__(self,num_classes=59):
        super(BasicModel, self).__init__()
        self.pool1 = MaxPool2D(kernel_size=2,stride=2)
        self.conv1 = Conv2D(in_channels=3,out_channels=num_classes,kernel_size=1)

    #input图像的输入
    def forward(self,inputs):
        x = self.pool1(inputs)
        # x = fluid.layers.
        x = self.conv1(x)

        return x


def main():
    with fluid.dygraph.guard(fluid.CUDAPlace(0)):
        model = BasicModel(num_classes=59)
        #model.eval()预测模式
        model.train()#训练模式
        input_data =np.random.rand(1,3,8,8).astype(np.float32)
        print("input data shape:",input_data.shape)
        input_data = to_variable(input_data)
        output_data = model(input_data)
        #将输出的output_data转化为np.arry
        output_data = output_data.numpy()
        print("out data shape:",output_data.shape)









if __name__ == '__main__':
    main()