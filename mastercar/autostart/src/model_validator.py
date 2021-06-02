# -*- coding: utf-8 -*-

import sys
import json
import datetime

import cv2
import numpy as np
import datetime

import predictor_wrapper

engine = "PaddleLite"
THRESHOLD = 0.6

cnn_args = {
    "shape": [1, 3, 128, 128]
}

yolo_args = {
    "shape": [1, 3, 300, 300]
}
def draw_line(img,angle,a):
    img = cv2.putText(img,str(angle), (50, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
    # filename = './line_images/' + str(a) + '.jpg'
    # cv2.imwrite(filename, img)
    return img
def draw_boxes(img, valid_results,a):
    """ draw SSD boxes on image"""
    if valid_results is None:
        return img
    res = list(img.shape)
    for item in valid_results:
        if item[1] < THRESHOLD:
            continue;
        print("name:",item[0],"   ","score:",item[1])
        bbox = item[2]
        left = bbox[0] * res[1]
        top = bbox[1] * res[0]
        right = bbox[2] * res[1]
        bottom = bbox[3] * res[0]
        start_point = (int(left), int(top))
        end_point = (int(right), int(bottom))
        color = (204, 0, 204)
        thickness = 2
        img = cv2.rectangle(img, start_point, end_point, color, thickness)
        img = cv2.putText(img,item[0], (400, 400), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
    # filename = './images/'+str(a)+'.jpg'
    # cv2.imwrite(filename, img)
    return img


def dataset(frame, size):
    frame = cv2.resize(frame, (size, size))
    lower_hsv = np.array([25, 75, 190])
    upper_hsv = np.array([40, 255, 255])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
    img = mask
    img = np.array(img).astype(np.float32)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    print("image_shape:", img.shape)
    return img;

def preprocess(args, img):
    """ preprocess image using formula y = (x - mean) x scale """
    shape = args["shape"]
    print(shape)
    img = dataset(img, shape[2]);

    shape = args["shape"]
    hwc_shape = list(shape)
    hwc_shape[3], hwc_shape[1] = hwc_shape[1], hwc_shape[3]
    data = np.zeros(hwc_shape).astype('float32')
    img = img.reshape(hwc_shape)
    data[0:, 0:hwc_shape[1], 0:hwc_shape[2], 0:hwc_shape[3]] = img
    if engine == "PaddlePaddle":
        data = data.transpose(0, 3, 1, 2)  # PaddlePaddle CHW;
    data = data.reshape(shape)
    return data

def yolo_preprocess(args, src):
    shape = args["shape"]
    img = cv2.resize(src, (shape[3], shape[2]))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32)
    img -= 127.5
    img *= 0.007843

    z = np.zeros((1, shape[2], shape[3], 3)).astype(np.float32)
    z[0, 0:img.shape[0], 0:img.shape[1] + 0, 0:img.shape[2]] = img
    z = z.reshape(1, 3, shape[3], shape[2]);
    return z;

def infer_cnn(predictor, image):
    data = preprocess(cnn_args, image)
    predictor.set_input(data, 0)
    predictor.run()
    out = predictor.get_output(0)
    print(out.data())

def infer_tiny_yolo(predictor, image):
    a = datetime.datetime.now()
    times = 100
    for i in range(times):
        data = yolo_preprocess(yolo_args, image)

    b = datetime.datetime.now()
    c = b - a
    print("proprocess used:{} ms".format(c.microseconds / 1000 / times))

    predictor.set_input(data, 0)

    print(image.shape)

    dims = np.array([image.shape[0], image.shape[1]]).astype("int32")
    dims = dims.reshape([1, 2])
    predictor.set_input(dims, 1)
    
    predictor.run()
    a = datetime.datetime.now()

    times = 100
    for i in range(times):
        predictor.run()
    
    b = datetime.datetime.now()
    c = b - a
    mill = c.microseconds / 1000.0;
    print("detection used:{} ms".format(mill / times))

    out = predictor.get_output(0)
    print(np.array(out))
    draw_boxes(image, np.array(out))

def create_predictor():
    if engine == "PaddlePaddle":
        return predictor_wrapper.PaddlePaddlePredictor()
    else:
        return predictor_wrapper.PaddleLitePredictor()

def main():
    cnn_predictor = create_predictor()
    print(cnn_predictor)
    # cnn_predictor.load("models/w1")
    yolo_predictor = create_predictor()
    print(yolo_predictor)
    # yolo_predictor.load("models/task")
    yolo_predictor.load("models/sign_fuse")
    # sign_fuse


    image_path = "0.png"

    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    # infer_cnn(cnn_predictor, img)
    infer_tiny_yolo(yolo_predictor, img)

# main()
