"""
   抓取豆瓣电影排行榜   （Agex动态加载）
    全站抓取 存入到mongoDB当中
"""
import re
import requests
import json
import time
import random
import pymongo
from fake_useragent import UserAgent

class DouBanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        self.i = 0
        self.con = pymongo.MongoClient('localhost',27017)
        self.db = self.con['doubandb']
        self.myset =self.db['doubanset']

    def get_html(self, url):
        """请求功能函数"""
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url, headers=headers).text
        return html

    def parse_html(self, url):
        # json.loacds  注意
        html = json.loads(self.get_html(url))
        #注意item的位置
        for one in html:
            item = {}
            item['name'] = one['title']
            item['time'] = one['release_date']
            item['score'] = one['score']
            print(item)
            self.i += 1
            #每执行一次insert_one就生成一个id
            self.myset.insert_one(item)

    def run(self):
        dict = self.get_all_type()
        menu = ''
        for one in dict:
            menu += one + '|'
        print(menu)
        c = input("请输入电影类别:")
        total = self.get_total(dict[c])
        for start in range(0, total, 20):
            url = self.url.format(dict[c], start)
            self.parse_html(url)
            time.sleep(random.uniform(0, 1))
        print("数量:", self.i)

    def get_total(self, type):
        """获取电影总数"""
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type)
        html = json.loads(self.get_html(url))
        total = html['total']
        return total

    def get_all_type(self):
        """获取所有电影类别分类type的值"""
        html = self.get_html('https://movie.douban.com/chart')
        regex = '<a href=.*?type_name=(.*?)&type=(.*?)&interval_id=100:90&action='
        pattern = re.compile(regex, re.S)
        # r_list =[(剧情，11),(爱情，..),()]
        r_list = pattern.findall(html)
        all_dict = {}
        for r in r_list:
            all_dict[r[0]] = r[1]
        return all_dict


if __name__ == '__main__':
    spider = DouBanSpider()
    spider.run()









