import os
import numpy as np
import paddle.fluid as fluid
import paddle.fluid.dygraph as dygraph
import random
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

def main():
    batch_size = 5
    with dygraph.guard(fluid.CUDAPlace(0)):
        transform = TransForm(256)
        basic_dataloader = BasicDataLoader(img_folder='./dummy_data',
                                           img_list_file='./dummy_data/list.txt',
                                           transform=transform,
                                           shuffle=True)
        dataloader = basic_dataloader()
        num_epoch = 2
        for epoch in range(1,num_epoch+1):
            for idx,(data,label) in enumerate(dataloader):
                model = BasicModel(num_classes=59)
                # model.eval()预测模式
                model.train()  # 训练模式
                input_data = np.random.rand(1, 3, 8, 8).astype(np.float32)
                print("input data shape:", input_data.shape)
                input_data = to_variable(input_data)
                output_data = model(input_data)
                # 将输出的output_data转化为np.arry
                output_data = output_data.numpy()
                print("out data shape:", output_data.shape)



if __name__ == '__main__':
    main()