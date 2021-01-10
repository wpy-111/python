"""
    行政区划分代码抓取
"""
import re
import sys
import requests
import redis
from lxml import etree
from hashlib import md5

class MzbSpider:
    def __init__(self):
        self.url ='http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
        self.r = redis.Redis(host='localhost',port=6379, db=0)
    def get_html(self,url):
        html = requests.get(url=url,headers=self.headers).text
        return html
    def xpath_func(self,html,xpath_dbs):
        p = etree.HTML(html)
        r_list = p.xpath(xpath_dbs)
        return r_list
    def md5_url(self,url):
        """对地址进行加密处理"""
        s = md5()
        s.update(url.encode())
        return s.hexdigest
    def parse_html(self):
        html_one = self.get_html(self.url)
        xpath ='//table/tr[1]/td[2]/a/@href'
        l_list = self.xpath_func(html_one,xpath)
        if l_list:
            url_two = 'http://www.mca.gov.cn' + l_list[0]
            #着手增量
            finger = self.md5_url(url_two)
            if self.r.sadd('mzb:fingers',finger):
                self.get_name_code(url_two)
            else:
                sys.exit("网站没更新")
        else:
            print("提取失败")

    def get_name_code(self,url_two):
        html_two = self.get_html(url_two)
        regex = r'window.location.href="(.*?)"'
        pattern = re.compile(regex,re.S)
        real_link = pattern.findall(html_two)
        if real_link:
            ture_url = real_link[0]
            self.get_data(ture_url)
        else:
            print("提取真是链接失败")
    def get_data(self,ture_url):
        html = self.get_html(ture_url)
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr[@height="19"]')
        for tr in tr_list:
            code_list = tr.xpath('./td[2]/text() | ./td[2]/span/text()')
            name_list = tr.xpath('./td[3]/text()')
            if code_list and name_list:
                code = code_list[0].strip()
                name = name_list[0].strip()
                print(code,name)
            else:
                print(code_list,name_list)

    def save_data(self):
        pass

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()

