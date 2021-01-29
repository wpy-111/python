"""
    文本分类
"""
import numpy as np
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
import sklearn.metrics as sm
import sklearn.model_selection as ms
train = sd.load_files('20news',encoding='latin1',random_state=7,shuffle=True)
print(type(train.data))#输入集
print(train.target[0])#每个文件的所属类别
#得到tfdif矩阵
cv = ft.CountVectorizer()
#获取词频
bow = cv.fit_transform(train.data)
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
print(tfidf.shape)
#数据集的划分
train_x,test_x,train_y,test_y = ms.train_test_split(tfidf,train.target,test_size=0.2,random_state=7)
#训练模型  基于多项分布的朴素贝叶斯
model = nb.MultinomialNB()
model.fit(train_x,train_y)
pre_y = model.predict(test_x)
print(sm.confusion_matrix(test_y,pre_y))
print(sm.classification_report(test_y,pre_y))
#业务应用
test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']
#将数据转成与训练样本格式一样的tfidf，才可以预测
bow = cv.transform(test_data)
test_tfidf = tt.transform(bow)
pre_test_y = model.predict(test_tfidf)
pre_prob = model.predict_proba(test_tfidf)
pre_prob = np.max(pre_prob,axis=1)
print(pre_test_y)
print(train.target_names)
for data,y,prob in zip(test_data,pre_test_y,pre_prob):
    print(data,'--->',train.target_names[y],prob)

