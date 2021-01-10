"""
    让西祠代理封掉ip

"""
from fake_useragent import UserAgent
import requests
url = 'http://www.xicidaili.com/cn/{}'
headers = {'User-Agent': UserAgent().random}
for i in range(1,1):
    url.format(i)
    res = requests.get(url=url,headers=headers)
    print(res.status_code)#打印响应码