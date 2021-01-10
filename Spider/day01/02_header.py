from urllib import request
"""
    测试网址发送请求 ，确认user——agent是什么
    测试结果：User-Agent": "Python-urllib/3.8
"""
res = request.urlopen('http://httpbin.org/get')
html = res.read().decode()
print(html)


