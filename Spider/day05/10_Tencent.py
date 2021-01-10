"""
  抓取腾讯招聘
"""
import requests
from fake_useragent import UserAgent
from lxml import etree
import json
import time
import random
class Tencent:
    def __init__(self):
        self.url = 'https://careers.tencent.com/search.html?index={}'

    def get_html(self,url):
        headers ={'User-Agent':UserAgent().random}
        html = requests.get(url=url,headers=headers).text
        return html
    def parese_html(self,html):
        pass
    def run(self):
        for i in range(1,2):
            url =self.url.format(i)
            html = self.get_html(url)
            print(html)
            with open('f.html','a')as f:
                f.write(html)
            time.sleep(random.uniform(1,2))
if __name__ == '__main__':
    spider = Tencent()
    spider.run()



