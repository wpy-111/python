# encoding=utf-8
import jieba
import sklearn.feature_extraction.text as ft

# jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# strs=["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学"]
# for str in strs:
#     seg_list = jieba.cut(str) # 使用paddle模式
#     print("Paddle Mode: " + '/'.join(list(seg_list)))

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
list = [' '.join(seg_list)]
print(list)
cv = ft.CountVectorizer()
bow = cv.fit_transform(list)
print(bow.toarray())
print(cv.get_feature_names())
tt = ft.TfidfTransformer()
tfidt = tt.fit_transform(bow)
print(tfidt.toarray())


# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
#载入字典
# # jieba.load_userdict('字典')
# jieba.suggest_freq('我在',True)
# print(", ".join(seg_list))
