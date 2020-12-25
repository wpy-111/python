"""
    百度贴吧————页数
"""

url = "http://tieba.baidu.com/f?kw=赵丽颖吧&pn={}"
for item in range(0,500,50):
    full_url = url.format(item)