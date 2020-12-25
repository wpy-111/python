"""
    爬取大众点评
"""
from queue import Queue
from threading import Thread,Lock
import time
import requests
from lxml import etree
from fake_useragent import UserAgent
from selenium import webdriver
class DaZhongSpider:
    def __init__(self):
        self.url = 'http://www.dianping.com/shanghai/ch10'
        self.headers = {'User-Agent': UserAgent().random}
        self.one_q = Queue()
    def xpath_func(self,html, xpath_dbs):
        p = etree.HTML(html)
        r_list = p.xpath(xpath_dbs)
        return r_list

    def get_html(self,url):
        html = requests.get(url=self.url,headers=self.headers).text
        return html
    def parse_oneurl(self):
        """将分裂页面地址放到队列中"""
        xpath= '//*[@id="classfy"]/a/span/text()'
        #//div/div//div[@id="classfy"]/a/span
        html = self.get_html(self.url)
        url_list = self.xpath_func(html,xpath)
        for url in url_list:
            print(url)
            self.one_q.put(url)
    def parse_twourl(self):
        while True:
            try:
                two_url = self.one_q.get(timeout=3)
                browser = webdriver.Chrome()
                browser.get(url=two_url)
                time.sleep(5)
            except Exception as e:
                print(e)
                break







if __name__ == '__main__':
    spider = DaZhongSpider()
    spider.parse_oneurl()





























