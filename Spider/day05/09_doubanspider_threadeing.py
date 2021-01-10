"""
   多线程抓取豆瓣电影
"""
from queue import Queue
import requests
import json
import time
import csv
from threading import Thread
from fake_useragent import UserAgent
class DouBanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={}&limit=20'
        self.q = Queue()
        self.i = 0
        self.f =    open('douban','a')
    def url_in(self):
        """让url地址入队列"""
        for start in range(0,376,20):
            url = self.url.format(start)
            self.q.put(url)
    def get_html(self,url):
        """请求功能函数"""
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url,headers=headers).text
        return html
    def parese_html(self):
        """线程事件函数"""
        while not self.q.empty():
            url = self.q.get()
            html = json.loads(self.get_html(url))
            for one in html:
                item = {}
                item['name'] = one['title']
                item['time'] = one['release_date']
                item['score'] = one['score']
                print(item)
                self.f.writelines(item)
                self.f.flush()
                self.i += 1
    def run(self):
        self.url_in()
        t_list = []
        for i in range(1):
            t = Thread(target=self.parese_html())
            t_list.append(t)
            t.start()

        for m in t_list:
            m.join()
        self.f.close()

if __name__ == '__main__':
    start_time = time.time()
    spider = DouBanSpider()
    spider.run()
    end_time = time.time()
    print("执行时间:%.2f"%(end_time-start_time))
#执行时间:11.12