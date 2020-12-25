"""
  贪婪匹配和非贪婪匹配
"""
import re
html = """
<div><p>如果你为们中弟子啥他一分，我便图你满门</p><div>
<div><p>更谁林楼中，如果你为们中弟子啥他一分，我便图你满门</p><div>
"""
#贪婪匹配
pattern = re.compile('<div><p>.*</p><div>',re.S)
r = pattern.findall(html)
print(r)
print("==========================")
# 非贪婪匹配  符合遇到最近的字符停止 <爬虫>专用
pattern = re.compile('<div><p>(.*?)</p><div>',re.S)
r = pattern.findall(html)
print(r)