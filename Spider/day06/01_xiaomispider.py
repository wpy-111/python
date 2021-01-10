"""
   小米应用商店，聊天社交应用  多线程抓取 注意哪操作全局变量，哪加锁
"""
import requests
import json
import time
import csv
from queue import Queue
from fake_useragent import UserAgent
from threading import Thread,Lock
class XiaoMiSpider:
    def __init__(self):
        self.url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.i = 1
        self.f = open('xiaomi.csv','a',encoding='utf-8')
        #创建csv的写入对象
        self.writer = csv.writer(self.f)
        #url队列
        self.q =Queue()
        #锁
        self.lock = Lock()
    def get_html(self,url):
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url,headers=headers).text
        return html
    def url_in(self):
        """让url地址入队列"""
        for page in range(67):
            page_url = self.url.format(page)
            self.q.put(page_url)

    def parse_html(self):
        """线程事件函数：get()"""
        while True:
            #加锁防止出现死锁
            self.lock.acquire()
            if not self.q.empty():
                url = self.q.get()
                self.lock.release()
                #请求加解析   动态数据一般都是json数据
                html = json.loads(self.get_html(url))
                item = {}
                one_page_list = []
                for app in html['data']:
                    item['name'] = app['displayName']
                    item['type'] = app['level1CategoryName']
                    item['link'] = app['packageName']
                    one_page_list.append((item['name'],item['type'],item['link']))
                    print(item)
                self.lock.acquire()
                self.writer.writerows(one_page_list)
                self.lock.release()
            else:
                self.lock.release()
                break

    def run(self):
        self.url_in()
        t_list = []
        for i in range(1):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()

        for iw in t_list:
            iw.join()

if __name__ == '__main__':
    spider = XiaoMiSpider()
    spider.run()

