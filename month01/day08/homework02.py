"""
   列表的函数
"""
#查找
list_result=["悟空", "", "唐僧", 56, 21, 85]
list02=["萨达","撒萨达","唐僧",85,21,85]
print(list_result.count("悟空"))#查找次数
print(list_result.index(21))#查找位置
# print(list01.pop(2))#删除末尾元素,有索引删除那一个元素
# print(list01)
# list01.extend(list02)#追加一个列表
# list01.clear()#清空列表
list03=[1,6,8,21,4,6,85,15]
list04=["s","a","d","s","x"]
list03.reverse()#改变列表的原先顺序反的，列表的反转
list04.sort()#默认按从小到大打顺序
list04.sort(reverse=False)#默认按从小到大打顺序
print(list03)
print(list04)
list05=[5,[5,5,68],85]
list06=list05.copy()
print(list06)