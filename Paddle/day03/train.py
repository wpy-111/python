import os
import paddle
import numpy as np
import cv2 as cv
import paddle.fluid as fluid

def transform_img(img):
    #图形的伸缩
    img = cv.resize(img,(224,224))
    img = np.transpose(img,(2,0,1))
    img = img.astype('float32')
    #将数据范围调正到【-1，1】
    img = img / 255
    img = img*2 - 1
    return img

def data_loader(datadir,batch_size=10,model='train'):
    filename = os.listdir(datadir)
    def reader():
        if model == 'train':
            np.random.shuffle(filename)
        batch_imges = []
        batch_label = []
        for name in filename:
            filepath = os.path.join(datadir,name)
            print(filepath)
            img = cv.imread(filepath)
            img = transform_img(img)
            if name[0] == 'H' or name[0] =='N':
                label = 0
            elif name[0]=='P' :
                label = 1
            else:
                raise ('File Error')
            batch_imges.append(img)
            batch_label.append(label)
            if len(batch_imges) == batch_size:
                imgs_arry = np.array(batch_imges).astype('float32')
                label_arry = np.array(batch_label).astype('float32').reshape(-1,1)
                yield imgs_arry,label_arry
                batch_imges = []
                batch_label = []
        if batch_imges>0:
            imgs_arry = np.array(batch_imges).astype('float32')
            label_arry = np.array(batch_label).astype('float32').reshape(-1, 1)
            yield imgs_arry, label_arry
    return reader

def train(model):
    with paddle.fluid.dygraph.guard():
        print("starting training")
        model.train()
        epoches = 5
        opt = paddle.fluid.optimizer.Momentum(learning_rate=0.001,momentum=0.9,parameter_list=model.paramters())
        train_loader = data_loader('..\\..\\..\\智能汽车数据集\\infer')
        for epoch in range(epoches):
            for batch_id,data in enumerate(train_loader()):
                x_data,y_data = data
                img = paddle.fluid.dygraph.to_variable(x_data)
                label = paddle.fluid.dygraph.to_variable(y_data)
                pre = model(img)
                loss = paddle.fluid.layers.sigmoid_cross_entropy_with_logits(pre,label)
                avg_loss = paddle.fluid.layers.mean(loss)
                if batch_id %10 ==0:
                    print("epoch:{},batch_id:{},loss is {}".format(epoch,batch_id,avg_loss.numpy()))
                avg_loss.backward()
                opt.minimize(avg_loss)
                model.clear_gradients()