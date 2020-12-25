"""
    使用独享代理来访问已经被封掉的西祠代理
"""
from fake_useragent import UserAgent
import requests
url = 'http://www.xicidaili.com/cn/1'
headers = {'User-Agent': UserAgent().random}
proxies={'http':'http://用户名:密码@ip地址',
            'https':'https://用户名:密码@ip地址'}
res = requests.get(url=url,property=proxies,headers=headers).text
print(res.status_code)#打印响应码











