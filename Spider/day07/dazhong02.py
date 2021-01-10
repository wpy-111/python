"""
    爬取大众点评
"""
from queue import Queue
from threading import Thread,Lock
import time
import json
import requests
from fake_useragent import UserAgent
from selenium import webdriver
class DaZhongSpider:
    def __init__(self):
        #cookie会过期
        self.url = 'http://www.dianping.com/member/1129917667'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                        'Cookie':'_lxsdk_cuid=17621c8c0aec8-0eeee41e338833-594a2011-144000-17621c8c0aec8; _lxsdk=17621c8c0aec8-0eeee41e338833-594a2011-144000-17621c8c0aec8; _hc.v=1562f060-1eba-bcde-d817-785529d993ab.1606884574; _dp.ac.v=e1e3b5a3-880f-4a46-932f-9c785c7791ac; ctu=5d385ad0f4ebf74fe10a602e62b0035a14924a5cf574a4724cc5d2f3fb95aa17; uamo=15834383659; fspop=test; cy=35; cye=taiyuan; s_ViewType=10; dper=bfdc3170fb462e4f4dc1d47f38731d48cb46b182b2e84cc54c0a88eca8b05d46acb4102520ac1b5becdf3c849838f3f7c23975ecb57e1da045c80996abb147044207580e0f31242df9b8137baf4396d51b64836c65613547dc078d8f17b169e5; ua=15834383659; dplet=05dddd95d523b553f1bea235cffdb562; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1606884574,1606892658; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606892667; _lxsdk_s=17622364df8-4c8-e30-eff%7C%7C213'}
    def get_html(self):
        html = requests.get(url=self.url,headers=self.headers).text
        print(html)

if __name__ == '__main__':
    spider = DaZhongSpider()
    spider.get_html()