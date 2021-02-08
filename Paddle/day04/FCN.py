"""
    FCN         full convolution network  全卷积网络
"""
import numpy as np
import paddle
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph
from paddle.nn import Conv2D, MaxPool2D, BatchNorm2D, Linear
from paddle.fluid.dygraph import to_variable

class FCN(dygraph.Layer):
    def __init__(self,num_classes = 59):
        super(FCN, self).__init__()
        in_channels = [3, 64, 128, 256, 512, 512]
        # 定义第一个卷积块，包含两个卷积
        self.conv1_1 = Conv2D(in_channels=in_channels[0], out_channels=in_channels[1], kernel_size=3, padding=100,
                              stride=1)
        self.conv1_2 = Conv2D(in_channels=in_channels[1], out_channels=in_channels[1], kernel_size=3, padding=1,
                              stride=1)
        # 定义第二个卷积块，包含两个卷积
        self.conv2_1 = Conv2D(in_channels=in_channels[1], out_channels=in_channels[2], kernel_size=3, padding=1,
                              stride=1)
        self.conv2_2 = Conv2D(in_channels=in_channels[2], out_channels=in_channels[2], kernel_size=3, padding=1,
                              stride=1)
        # 定义第三个卷积块，包含三个卷积
        self.conv3_1 = Conv2D(in_channels=in_channels[2], out_channels=in_channels[3], kernel_size=3, padding=1,
                              stride=1)
        self.conv3_2 = Conv2D(in_channels=in_channels[3], out_channels=in_channels[3], kernel_size=3, padding=1,
                              stride=1)
        self.conv3_3 = Conv2D(in_channels=in_channels[3], out_channels=in_channels[3], kernel_size=3, padding=1,
                              stride=1)
        # 定义第四个卷积块，包含三个卷积
        self.conv4_1 = Conv2D(in_channels=in_channels[3], out_channels=in_channels[4], kernel_size=3, padding=1,
                              stride=1)
        self.conv4_2 = Conv2D(in_channels=in_channels[4], out_channels=in_channels[4], kernel_size=3, padding=1,
                              stride=1)
        self.conv4_3 = Conv2D(in_channels=in_channels[4], out_channels=in_channels[4], kernel_size=3, padding=1,
                              stride=1)
        # 定义第五个卷积块，包含三个卷积
        self.conv5_1 = Conv2D(in_channels=in_channels[4], out_channels=in_channels[5], kernel_size=3, padding=1,
                              stride=1)
        self.conv5_2 = Conv2D(in_channels=in_channels[5], out_channels=in_channels[5], kernel_size=3, padding=1,
                              stride=1)
        self.conv5_3 = Conv2D(in_channels=in_channels[5], out_channels=in_channels[5], kernel_size=3, padding=1,
                              stride=1)

        # 使用Sequential 将卷积和relu组成一个线性结构（fc + relu）
        # 当输入为224x224时，经过五个卷积块和池化层后，特征维度变为[512x7x7]
        self.fc1 = paddle.nn.Sequential(paddle.nn.Linear(512 * 7 * 7, 4096), paddle.nn.ReLU())
        self.drop1_ratio = 0.5
        self.dropout1 = paddle.nn.Dropout(self.drop1_ratio, mode='upscale_in_train')
        # 使用Sequential 将卷积和relu组成一个线性结构（fc + relu）
        self.fc2 = paddle.nn.Sequential(paddle.nn.Linear(4096, 4096), paddle.nn.ReLU())

        self.drop2_ratio = 0.5
        self.dropout2 = paddle.nn.Dropout(self.drop2_ratio, mode='upscale_in_train')
        self.fc3 = paddle.nn.Linear(4096, 1)

        self.relu = paddle.nn.ReLU()
        self.pool = MaxPool2D(stride=2, kernel_size=2,ceil_mode=True)

        self.score = Conv2D(4096,num_classes,1)
        self.score_pool3 = Conv2D(256,num_classes,1)
        self.score_pool4 = Conv2D(512,num_classes,1)

        #定义上采样
        self.up_output = dygraph.Conv2DTranspose(num_channels=num_classes,num_filters=num_classes,filter_size=4,stride=2,bias_attr=False)
        self.up_pool4 = dygraph.Conv2DTranspose(num_channels=num_classes,num_filters=num_classes,filter_size=4,stride=2,bias_attr=False)
        self.up_final = dygraph.Conv2DTranspose(num_channels=num_classes,num_filters=num_classes,filter_size=16,stride=8,bias_attr=False)


    def forward(self, input):
        x = self.relu(self.conv1_1(input))
        x = self.relu(self.conv1_2(x))
        x = self.pool(x)

        x = self.relu(self.conv2_1(x))
        x = self.relu(self.conv2_2(x))
        x = self.pool(x)

        x = self.relu(self.conv3_1(x))
        x = self.relu(self.conv3_2(x))
        x = self.relu(self.conv3_3(x))
        x = self.pool(x)
        pool3 = x

        x = self.relu(self.conv4_1(x))
        x = self.relu(self.conv4_2(x))
        x = self.relu(self.conv4_3(x))
        x = self.pool(x)
        pool4 = x

        x = self.relu(self.conv5_1(x))
        x = self.relu(self.conv5_2(x))
        x = self.relu(self.conv5_3(x))
        x = self.pool(x)

        x = paddle.flatten(x, 1, -1)
        x = self.dropout1(self.relu(self.fc1(x)))
        x = self.dropout2(self.relu(self.fc2(x)))
        # x = self.fc3(x)

        x = self.score(x)
        x = self.up_output(x)
        up_out = x
        x = self.score_pool4(pool4)
        x = x[:,:,5:5+up_out.shape[2],5:5+up_out.shape[3]]

        up_pool4 = x
        x = up_pool4 + up_out
        x = self.up_pool4(x)
        up_pool4 = x

        x = self.score_pool3(pool3)
        x = x[:,:,9:9+up_pool4.shape[2],9:9+up_pool4.shape[3]]
        up_pool3 = x

        x = up_pool3+up_pool4

        x = self.up_final(x)
        x = x[:,:,31:31+input.shape[2],31:31+input.shape[3]]

        return x

with dygraph.guard():
    with dygraph.guard(fluid.CUDAPlace(0)):
        data = np.ones((2,3,512,512)).astype('float32')
        data = to_variable(data)
        model = FCN()
        model.eval()
        pre = model(data)
        print(pre.numpy().shape)

















