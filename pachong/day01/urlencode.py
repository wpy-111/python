"""
   百度搜素关键字，把响应内容保存到本地文件
"""
from urllib import request,parse
#1.拼接url地址：http://www.baidu.com/s?wd=xxx
word = input("请输入搜索内容")
params = parse.urlencode({'wd':word})
url = 'http://www.baidu.com/s?{}'.format(params)
headers={'User-Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
#2.创建请求对象  - Request()
req = request.Request(url=url,headers=headers)
#3.获取响应对象
res = request.urlopen(req)
#4.提取响应内容
html = res.read().decode()
#保存到本地文件
filename = word + '.html'
with open(filename,'w') as f:
    f.write(html)
print('ok')