import os
import numpy as np
import cv2 as cv

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
            cv.imshow('img',img)
            cv.waitKey()
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



train_loader = data_loader('..\..\..\智能汽车数据集\infer')
data_reader = train_loader()
print(next(data_reader))