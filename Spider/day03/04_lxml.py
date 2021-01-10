"""
  初始程序 -抓取猫眼电影top100  xpath  出来的都是列表
"""
import requests
from lxml import etree
import time
import random
# from lxml import e
class MaoYanSpider:
    def __init__(self):
        self.url = "https://trade.maoyan.com/board/4?offset={}"
        self.header = {'User-Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
        self.count=0
    def get_html(self,url):
        html = requests.get(url=url,headers=self.header).text
        self.parse_html(html)
    def parse_html(self,html):
        """提取数据函数"""
        #1.创建解析对象
        p = etree.HTML(html)
        #2.基准的xpath，得到十个dd节点对象的列表
        dd_list = p.xpath('//dl[@class="board-wrapper"]/dd')
        item = {}
        for dd in dd_list:
            item['name'] = dd.xpath('.//p[@class="name"]/a/text()')[0].strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print(item)
            self.count += 1
            # self.save_html(r_list)
    def save_html(self,r_list):
        item={}
        for i in r_list:
            item["name"] = i[0].strip()
            item["star"] = i[1].strip()
            item["time"] = i[2].strip()
            print(item)
            self.count+=1

    def run(self):
        """程序入口"""
        for i in range(0,91,10):
            url = self.url.format(i)
            self.get_html(url)
            time.sleep(random.uniform(0,1))
        print(self.count)
if __name__ == '__main__':
    start_time = time.time()
    spider = MaoYanSpider()
    spider.run()
    end_time = time.time()
    print("执行时间：%.2f"%(end_time-start_time))
