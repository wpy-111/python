"""
    向测试网站发送请求
"""
import requests
url = 'http://httpbin.org/get'
headers = {'User-Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
res = requests.get(url=url,headers=headers)
#text 获取相应内容 字符串  全是属性
html = res.text
#content 获取相应内容 字节串  全是属性
r = res.content
print(type(r))
#url 返回实际数据的地址
print(res.url)
#status_code:返回http响应码
print(res.status_code)