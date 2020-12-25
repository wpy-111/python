"""
  math对象说明
"""
import re
pattern =r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search("abcdefgh123456")
#属性变量
print(obj.pos)#目标字符串开始位置
print(obj.endpos)#目标字符串的结束位置
print(obj.lastgroup)#最后一组名
print(obj.lastindex)#最后一组序号
print("==================================")
#属性方法
print(obj.span())#匹配内容的起止位置
print(obj.start())
print(obj.end())
print(obj.groupdict())#捕获组字典  命名的
print(obj.groups())#子组对应的内容
print(obj.group())#获取math对象对应内容
