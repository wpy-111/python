"""
    语音识别
    1.读取训练样本数据，98哥样本分属于七类
    2.吧九十八个文件的mfcc特征，与相应类别标签配对，整理样本数据集
    3.选择分类模型进行训练
    os.path.sep默认路径分隔符
"""
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
import sklearn.svm as svm
import sklearn.metrics as sm
import os
import sklearn.preprocessing as sp
#封装函数读取音频
def search_files(filepath):
    """
    加载filepath下所有文件信息，并返回整理{apple：【url】}
    """
    objects = {}
    for curdir,subdirs,files in os.walk(filepath):
        for f in files:
            dir = curdir.split(os.path.sep)[-1]
            if dir not in objects.keys():
                objects[dir] = []
            objects[dir].append(os.path.join(curdir,f))
    return objects
object = search_files('.\\20news')

# #整理训练集数据
x,y = [],[]
for label,urls in object.items():
    for url in urls:
        with open(url,'r',encoding='utf-8') as f:
            mfcc = f.read()
        sample_rate,sigs = wf.read(url)
        mfcc = sf.mfcc(sigs,sample_rate)
        mfcc = np.mean(mfcc,axis=0)
        x.append(mfcc)
        y.append(label)
x = np.array(x)
y = np.array(y)
encoder = sp.LabelEncoder()
y = encoder.fit_transform(y)
model =svm.SVC(kernel='linear',probability=True)
model.fit(x,y)
pre_test_y = model.predict(x)
#输出混淆矩阵
print(sm.confusion_matrix(y,pre_test_y))
#输出分类报告
print(sm.classification_report(y,pre_test_y))
#输出每个样本的置信概率
probs = model.predict_proba(x)
for y1,y2,p in zip(y,pre_test_y,np.max(probs,axis=1)):
    print(y1,y2,p)

