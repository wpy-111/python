import jieba
list = jieba.cut('我在清华大学学科院上学',cut_all=True)# 全模式
print('/'.join(list))
list = jieba.cut('我在清华大学学科院上学',cut_all=False)# 精确模式
print('/'.join(list))
list = jieba.cut('我在清华大学学科院上学')# 精确模式
print('/'.join(list))
list = jieba.cut_for_search('我在清华大学学科院上学')#搜索引擎模式
print('/'.join(list))