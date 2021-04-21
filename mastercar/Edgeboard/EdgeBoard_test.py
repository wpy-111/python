#!usr/bin/python3
#_*_coding:utf-8_*_
# USAGE
# python deep_learning_object_detection.py --image images/example_01.jpg \
#	--prototxt MobileNetSSD_deploy.prototxt.txt --__model__ MobileNetSSD_deploy.caffemodel

# import the necessary packages
import numpy as np
import argparse
import cv2
import time

def ad_threshold(img):
    img = cv2.medianBlur(img, 5)
    img = cv2.GaussianBlur(img, (3, 3), 0)  # 降噪处理
    th2 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 4)
    return th2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()#获取所有参数
ap.add_argument("-i", "--image", required=False,#第一个参数
	help="path to input image")#输入图像路劲
ap.add_argument("-p", "--prototxt", required=False,default='MobileNetSSD_deploy.prototxt.txt',#第二个参数
	help="path to Caffe 'deploy' prototxt file")#Caffe 'deploy' prototxt文件的路径
ap.add_argument("-m", "--__model__", required=False,default="MobileNetSSD_deploy.caffemodel",#第三个参数
	help="path to Caffe pre-trained __model__")#通往Caffe预训练模型的路径
ap.add_argument("-c", "--confidence", type=float, default=0.2,#第四个参数
	help="minimum probability to filter weak detections")#最小概率过滤弱检测
args = vars(ap.parse_args())#里面函数解析所有参数
print(args)
# initialize the list of class labels MobileNet SSD was trained to （初始化MobileNet SSD受训到的类标签列表）
# detect, then generate a set of bounding box colors for each class（检测，然后为每个类生成一组边框颜色）
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
#功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
# size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出m*n*k个样本，缺省时输出1个值。
# load our serialized __model__ from disk
print("[INFO] loading __model__...")
net1 = cv2.dnn.readNetFromCaffe(args["prototxt"], args["__model__"])
net2 = cv2.dnn.readNetFromCaffe(args["prototxt"], args["__model__"])
# cv2.dnn.readNetFromCaffe(prototxt, __model__)  用于进行SSD网络的caffe框架的加载
# 参数说明:prototxt表示caffe网络的结构文本，model表示已经训练好的参数结果

# load the input image and construct an input blob for the image（加载输入图像，并为该图像构建一个输入blob）
# by resizing to a fixed 300x300 pixels and then normalizing it（将大小调整为固定的300x300像素，然后将其规格化）
# (note: normalization is done via the authors of the MobileNet SSD
# implementation)（注意:标准化是通过MobileNet SSD实现的作者完成的）
screen_name1="test_camera1"
screen_name2="test_camera2"
# cv2.namedWindow(screen_name1,cv2.WINDOW_NORMAL)（窗口大小可以改变：）
# cv2.namedWindow(screen_name2,cv2.WINDOW_NORMAL)
# cv2.setWindowProperty(screen_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)（动态更改窗口的参数。）
# cv2.resizeWindow(screen_name1,640,480)
# cv2.resizeWindow(screen_name2,640,480)
cap1=None
cap2=None
ok1=False
ok2=False
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
while True:
	ok1, frame1 = cap1.read()  # 读取每一帧图片
	ok2, frame2 = cap2.read()  # 读取每一帧图片
	if not (ok1 and ok2):
		break
	# 转换为灰度图
	# image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# image = ad_threshold(gray)#降噪处理
	image1 =frame1
	image2 = frame2
	(h1, w1) = image1.shape[:2]
	(h2, w2) = image2.shape[:2]
	#cv2.dnn.blobFromImage()对图像进行预处理，包括减均值，比例缩放，裁剪，交换通道等，返回一个4通道的blob(blob可以简单理解为一个N维的数组，用于神经网络的输入
	blob1 = cv2.dnn.blobFromImage(cv2.resize(image1, (300, 300)), 0.007843, (300, 300), 127.5)
	blob2 = cv2.dnn.blobFromImage(cv2.resize(image2, (300, 300)), 0.007843, (300, 300), 127.5)
	# pass the blob through the network and obtain the detections and（将blob通过网络，得到检测和）
	# predictions
	print("[INFO] computing object detections...")
	net1.setInput(blob1)
	net2.setInput(blob2)
	detections1 = net1.forward()
	detections2 = net2.forward()
	# loop over the detections
	for i in np.arange(0, detections1.shape[2]):
		# extract the confidence (i.e., probability) associated with the
		# prediction
		confidence = detections1[0, 0, i, 2]
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > args["confidence"]:
			# extract the index of the class label from the `detections`,
			# then compute the (x, y)-coordinates of the bounding box for
			# the object
			idx = int(detections1[0, 0, i, 1])
			box = detections1[0, 0, i, 3:7] * np.array([w1, h1, w1, h1])
			(startX, startY, endX, endY) = box.astype("int")

			# display the prediction
			label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
			print("[INFO] {}".format(label))
			cv2.rectangle(image1, (startX, startY), (endX, endY),
						  (0, 200, 0), 2)
			y = startY - 15 if startY - 15 > 15 else startY + 15
			cv2.putText(image1, label, (startX, y),
						cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 0), 2)
	for i in np.arange(0, detections2.shape[2]):
		# extract the confidence (i.e., probability) associated with the
		# prediction
		confidence = detections2[0, 0, i, 2]
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > args["confidence"]:
			# extract the index of the class label from the `detections`,
			# then compute the (x, y)-coordinates of the bounding box for
			# the object
			idx = int(detections2[0, 0, i, 1])
			box = detections2[0, 0, i, 3:7] * np.array([w1, h1, w1, h1])
			(startX, startY, endX, endY) = box.astype("int")

			# display the prediction
			label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
			print("[INFO] {}".format(label))
			cv2.rectangle(image2, (startX, startY), (endX, endY),
						  (0, 200, 0), 2)
			y = startY - 15 if startY - 15 > 15 else startY + 15
			cv2.putText(image2, label, (startX, y),
						cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 0), 2)
	# show the output image
	imghstack = np.hstack((image1, image2))
	cv2.imshow(screen_name1, imghstack)
	# cv2.imshow(screen_name2, image2)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break
	if cv2.getWindowProperty(screen_name1,1)<0 :
		break
cap1.release()
# cap2.release()
cv2.destroyAllWindows()