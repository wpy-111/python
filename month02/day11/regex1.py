"""
   正则  产生math对象
"""
import re
s = "今天是2020年10月1日，"\
    " 2020年的愿望实现了吗？"
pattern = r"\d+"
#获取匹配内容的迭代器
result = re.finditer(pattern,s)
for i in result:
    #迭代得到每处匹配内容的math对象
    print(i.group())

#完全匹配
pattern1 = r".+"
obj = re.fullmatch(pattern1,s)
print(obj.group())

#匹配开始位置
pattern2 = r"\w+"
obj1 = re.match(pattern2,s)
print(obj1.group())

#匹配第一处
pattern3 = r"\d+"
obj3= re.search(pattern3,s)
print(obj3.group())
