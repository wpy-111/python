import os
import numpy as np
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph
import random
import paddle
import cv2 as cv
from paddle.fluid.dygraph import to_variable
from paddle.nn import Conv2D, MaxPool2D, Linear, Dropout

class TransForm(object):
    def __init__(self,size=256):
        self.size = size

    def __call__(self,input,label):
        input = cv.resize(input,(self.size,self.size),interpolation=cv.INTER_LINEAR)
        label = cv.resize(label,(self.size,self.size),interpolation=cv.INTER_NEAREST)
        return input,label

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

class BasicDataLoader(object):
    def __init__(self,
                 img_folder,
                 img_list_file,
                 transform = None,
                 shuffle=True):
        self.img_folder = img_folder
        self.img_list_file = img_list_file
        self.transform = transform
        self.shuffle = shuffle
        self.data_list = self.read_list()

    def read_list(self):
        data_list = []
        with open(self.img_list_file) as  infile:
            for line in infile:
                data_path = os.path.join(self.img_folder,line.split()[0])
                label_path = os.path.join(self.img_folder,line.split()[1])
                data_list.append((data_path,label_path))
        if self.shuffle:
            random.shuffle(data_list)
        return data_list

    def preprocess(self,data,label):
        h,w,c = data.shape
        h_gt,w_gt = label.shape
        assert h==h_gt, "Error"
        assert w==w_gt, "Error"
        if self.transform:
            data,label = self.transform(data,label)
        label = label[:,:,np.newaxis]
        return data,label

    def __len__(self):
        return len(self.data_list)
    def __call__(self, *args, **kwargs):
        for data_path,label_path in self.data_list:
            data = cv.imread(data_path)
            data = cv.cvtColor(data,cv.COLOR_BGR2RGB)
            label = cv.imread(label_path,cv.IMREAD_GRAYSCALE)
            print(data.shape,label.shape)
            data,label = self.preprocess(data,label)
            yield data,label


from paddle.io import Dataset


def data_generator(dataloader,batch_size):
    # 训练模式下，打乱训练数据
    imgs_list = []
    labels_list = []
    # 按照索引读取数据
    for img,label in dataloader:
        imgs_list.append(img)
        labels_list.append(label)
        # 如果当前数据缓存达到了batch size，就返回一个批次数据
        if len(imgs_list) == batch_size:
            yield np.array(imgs_list), np.array(labels_list)
            # 清空数据缓存列表
            imgs_list = []
            labels_list = []

    # 如果剩余数据的数目小于BATCHSIZE，
    # 则剩余数据一起构成一个大小为len(imgs_list)的mini-batch
    if len(imgs_list) > 0:
        yield np.array(imgs_list), np.array(labels_list)

def main():

    with dygraph.guard(fluid.CUDAPlace(0)):
        model = FCN(num_classes=59)
        # model.eval()预测模式
        model.train()  # 训练模式
        transform = TransForm(256)
        basic_dataloader = BasicDataLoader(img_folder='./dummy_data',
                                           img_list_file='./dummy_data/list.txt',
                                           transform=transform,
                                           shuffle=True)
        dataloader = basic_dataloader()
        train_dataloader = data_generator(dataloader,batch_size=5)
        num_epoch = 2
        opt = paddle.fluid.optimizer.Momentum(learning_rate=0.001, momentum=0.9, parameter_list=model.paramters())
        for epoch in range(1,num_epoch+1):
            for batch_id,data in enumerate(train_dataloader):
                for idx,(img,label) in enumerate(data):

                    img = fluid.layers.transpose(img,(0,3,2,1))
                    label = fluid.layers.transpose(label,(0,3,2,1))
                    predicts = model(img)
                    # 计算损失
                    loss = fluid.layers.sigmoid_cross_entropy_with_logits(predicts,label)
                    avg_loss = fluid.layers.mean(loss)
                    if idx % 20 == 0:
                        print("epoch: {}, iter: {}, loss is: {}".format(epoch, idx, avg_loss.numpy()))
                    # 反向传播
                    avg_loss.backward()
                    # 最小化loss,更新参数
                    opt.minimize(avg_loss)
                    # 清除梯度
                    model.clear_gradients()

if __name__ == '__main__':
    main()