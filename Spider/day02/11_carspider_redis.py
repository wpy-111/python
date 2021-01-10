"""
   抓取汽车之家二手车的信息
"""
from urllib import request,parse
import re
import time
import random
from hashlib import md5
import redis
import sys

class CarSpoder:
    def __init__(self):
        #一级url地址
        self.url = "https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/"
        self.headers={'User-Agent':"Opera Win7:Opera/9.80 (Windows NT 6.1; U;zh-cn) Presto/2.9.168 Version/11.50"}
        self.r = redis.Redis(host='localhost',port = 6379,db=0)
    #功能函数1 -获取html
    def get_html(self,url):
        res = request.Request(url=url,headers=self.headers)
        req = request.urlopen(res)
        html = req.read().decode('gb2312','ignore')
        return html
    #功能函数2.-正则解析
    def re_func(self,regex,html):
        pattern = re.compile(regex,re.S)
        r_list = pattern.findall(html)
        return r_list
    def md5_func(self,string):
        s = md5()
        s.update(string.encode())
        return s.hexdigest()
    def pares_html(self,one_url):
        #1.先从一级响应提取链接
        one_html = self.get_html(one_url)

        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        href_list = self.re_func(one_regex,one_html)
        #2.依次发送请求链接
        for href in href_list:
            two_url = "http://www.che168.com"+href
            finger = self.md5_func(two_url)
            if self.r.sadd('car:fingers',finger) ==1:
                self.get_car_infor(two_url)
                #爬完一辆休眠
                time.sleep(random.uniform(0, 1))
            else:
                sys.exit('更新完成')
    def get_car_infor(self,two_url):
        #获取第一辆车的详细信息
        two_html = self.get_html(two_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b'
        item = {}
        car_list = self.re_func(two_regex,two_html)
        item['name'] = car_list[0][0]
        item['km'] = car_list[0][1]
        item['year'] = car_list[0][2]
        item['type'] = car_list[0][3].split('/')[0]
        item['diplace'] = car_list[0][3].split('/')[1]
        item['city'] = car_list[0][4]
        item['price'] = car_list[0][5]
        print(item)
    def run(self):
        for i in range(1,5):
            one_url =self.url.format(i)
            self.pares_html(one_url)

if __name__ == '__main__':
    car = CarSpoder()
    car.run()







