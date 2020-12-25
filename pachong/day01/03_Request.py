"""
   包装请求，向测试网站发送请求
"""
from urllib import request
url='http://httpbin.org/get'
headers={'User-Agent':"Win7:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
#1.创建请求对象  - Request()
req = request.Request(url=url,headers=headers)
#2.获取响应对象
res = request.urlopen(req)
#3.提取响应内容
html = res.read().decode()
print(html)