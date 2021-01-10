"""
   抓取豆瓣电影排行榜   （Agex动态加载）

"""
import requests
import json
import time
import random
from fake_useragent import UserAgent
class DouBanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={}&limit=20'
        self.i = 0

    def get_html(self,url):
        """请求功能函数"""
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url,headers=headers).text
        return html

    def parse_html(self,url):
        #json.loacds  注意
        html = json.loads(self.get_html(url))
        item = {}
        for one in html:
            item['name'] = one['title']
            item['time'] = one['release_date']
            item['score'] = one['score']
            print(item)
            self.i += 1

    def run(self):
        total = self.get_total()
        for start in range(0,total,20):
            url =self.url.format(start)
            self.parse_html(url)
            time.sleep(random.uniform(0,1))
        print("数量:",self.i)

    def get_total(self):
        """获取电影总数"""
        url = 'https://movie.douban.com/j/chart/top_list_count?type=13&interval_id=100%3A90'
        html = json.loads(self.get_html(url))
        total = html['total']

        return total
if __name__ == '__main__':
    spider = DouBanSpider()
    spider.run()






