"""
   代理ip  访问测试网站
"""
import requests
url = 'http://httpbin.org/get'
headers = {'User-Agent':'xxxxx'}
proxies = {'http':'http://222.95.241.44:3000'
           ,'https':'https://222.95.241.44:3000'}

html = requests.get(url=url,headers=headers,proxies=proxies).text
print(html)
"""

    代理ip异常
    1.连不上代理ip：瞬间抛出异常proxyError
    2.连接上了代理ip，但是代理ip不能访问网站

"""