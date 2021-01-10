"""
    建立自己的代理池

"""
"""
  建立私密代理的代理池ip
"""
import requests
from fake_useragent import UserAgent


class ProxyPool:
    def __init__(self):
        self.url = 'http://www.goubanjia.com/'
        self.f = open('proxy.txt', 'a')
        self.headers = {'User-Agent': UserAgent().random}

    def get_proxy(self):
        html = requests.get(url=self.url, headers=self.headers).text
        # proxy_list[代理ip]
        proxy_list = html.split('\r\n')
        for proxy in proxy_list:
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        proxies = {
            'http': 'http://用户名:密码@{}'.format(proxy),
            'https': 'https://用户名:密码@{}'.format(proxy)
        }
        try:
            html = requests.get(url=self.url, proxies=proxies, headers=self.headers, timeout=3).text
            print(proxies, '\33[31m可用\033[0m')
            self.f.write(proxy + '\n')
        except Exception as e:
            print(proxies, "不可用")

    def run(self):
        self.get_proxy()


if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()

