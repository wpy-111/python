"""
    tfdif 词频逆文档矩阵
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.feature_extraction.text as ft
import nltk.tokenize as tk
doc ='The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
sents = tk.sent_tokenize(doc)
print(sents)
#提取词袋矩阵
vc = ft.CountVectorizer()
bow = vc.fit_transform(sents)
#bow拿到的是稀疏矩阵
print(bow)
print(bow.toarray())
#拿到特征名字
print(vc.get_feature_names())
#获取tfidf  每一个数值是对每一句话的贡献程度
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
print(np.round(tfidf.toarray(),2))