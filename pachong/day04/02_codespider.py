"""
   抓取tedu的笔记
   使用auth参数
"""
import requests
import os
import time
import random
from lxml import etree
from fake_useragent import UserAgent
class CodeSpider:
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid2004/04_month05_spider/'
        self.auth = ('tarenacode','code_2013')
        self.directory = '/home/tarena/'+self.url[26:]
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def  parse_html(self):
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=self.url,auth=self.auth,headers=headers).text
        p = etree.HTML(html)
        href_list = p.xpath('//a/text()')
        for href in href_list:
            if href.endswith('.zip'):
                self.download_link(href)
                time.sleep(random.uniform(1,2))
    def download_link(self,href):
        url1 = self.url+href
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url1,auth=self.auth,headers=headers).content
        filename = self.directory+href
        with open(filename,'wb')as f:
            f.write(html)
        print(filename,"下载成功")
    def run(self):
        self.parse_html()
if __name__ == '__main__':
    spider = CodeSpider()
    spider.run()


