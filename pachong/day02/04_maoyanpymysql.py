"""
  初始程序 -抓取猫眼电影top100 保存到pymsql
"""
from urllib import request,parse
import re
import time
import random
import pymysql
class MaoYanSpider:
    def __init__(self):
        self.url = "https://trade.maoyan.com/board/4?offset={}"
        self.header = {'User-Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
        self.count=0
        self.db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'maoyandb',
                     charset = 'utf8'
            )
        self.cur = self.db.cursor()
    def get_html(self,url):
        req = request.Request(url=url,headers=self.header)
        res = request.urlopen(req)
        html = res.read().decode('utf-8','ignore')
        self.parse_html(html)
    def parse_html(self,html):
        """提取数据函数"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(regex,re.S)
        r_list = pattern.findall(html)
        print(r_list)
        self.save_html(r_list)
    def save_html(self,r_list):
        for i in r_list:
            li =[i[0].strip(),
                 i[1].strip(),
                 i[2].strip()]

            ins = "insert into maoyantab values(%s,%s,%s)"
            self.cur.execute(ins,li)
            self.db.commit()
            self.count += 1

    def run(self):
        """程序入口"""
        for i in range(0,91,10):
            url = self.url.format(i)
            self.get_html(url)
            time.sleep(random.uniform(0,1))
        print(self.count)
        self.cur.close()
        self.db.close()
if __name__ == '__main__':
    start_time = time.time()
    spider = MaoYanSpider()
    spider.run()
    end_time = time.time()
    print("执行时间：%.2f"%(end_time-start_time))
