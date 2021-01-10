"""
  初始程序 -抓取猫眼电影top100  保存 到csv中
"""
from urllib import request,parse
import re
import time
import random
import csv
class MaoYanSpider:
    def __init__(self):
        self.url = "https://trade.maoyan.com/board/4?offset={}"
        self.header = {'User-Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
        #计数
        self.count=0
        self.f = open("maoyan01.csv",'a')
        self.writer = csv.writer(self.f)
    def get_html(self,url):
        req = request.Request(url=url,headers=self.header)
        res = request.urlopen(req)
        html = res.read().decode('gb18030','ignore')
        self.parse_html(html)
    def parse_html(self,html):
        """提取数据函数"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(regex,re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)
    def save_html(self,r_list):
        for file in r_list:
            #去除空白
            li=[file[0].strip(),file[1].strip(),file[2].strip()]
            print(li)
            self.writer.writerow(li)
            self.count+=1

    def run(self):
        """程序入口"""
        for i in range(0,91,10):
            url = self.url.format(i)
            self.get_html(url)
            time.sleep(random.uniform(0,1))
        print(self.count)
        self.f.close()
if __name__ == '__main__':
    start_time = time.time()
    spider = MaoYanSpider()
    spider.run()
    end_time = time.time()
    print("执行时间：%.2f"%(end_time-start_time))
