"""
  regex.py  re模块功能
"""
import re
#目标字符串
s ="Alex:1997,Sunny:1999"
#正则表达式
pattern = r"\w+:\d+"
# l = re.findall(pattern,s)#正则表达式中的子组
# print(l)

#用compile
regex = re.compile(pattern)
l = regex.findall(s,0,8)#s[0:8]
print(l)

#分割字符串
m = re.split(r'[,:]',s)
print(m)

#字符串替换re.sub(pattern,replace,string,count,flags = 0)
# 功能: 使用一个字符串替换正则表达式匹配到的内容
# 参数: pattern  正则表达式
#      replace  替换的字符串
#      string 目标字符串
#      count  最多替换几处,默认替换全部
#      flags  功能标志位,扩展正则表达式的匹配
# 返回值: 替换后的字符串
x = re.sub(r':','-',s,1)
c = re.subn(r':','-',s,1)
print(x)
print(c)#返回值多了一个替换次数