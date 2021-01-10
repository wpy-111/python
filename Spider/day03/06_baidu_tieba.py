"""
    抓取图片百度贴吧  自己写的
"""
from lxml import etree
import time
import random
import requests
from urllib import parse
import os
class BaiDu:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
        self.mes = input("请输入贴吧名：")
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'
        self.directory = '/home/tarena/baidu/{}/'.format(self.mes)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
    def get_html(self,url):
        html = requests.get(url=url,headers=self.headers).text
        self.parse_html(html)
    def parse_html(self,html):
        p = etree.HTML(html)
        add_list = p.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        for add in add_list:
            url_two = 'http://tieba.com'+add
            self.get_two_html(add,url_two)
            time.sleep(random.uniform(0,2))
    def get_two_html(self,add,url_two):
        html_two =requests.get(url=url_two,headers = self.headers).content
        p2 = etree.HTML(html_two)
        picture_list = p2.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video')
        if picture_list:
            self.save_picture(add,picture_list[0])
        else:
            print('wu')
    def save_picture(self,add,picture):
        html = requests.get(url=picture,headers=self.headers).content
        filename = '{}{}.jpg'.format(self.directory,add[-5:])
        with open(filename,'wb')as f:
            f.write(html)
        print(filename, "下载成功")

    def run(self):
        for i in range(0,500,50):
            name = parse.quote(self.mes)
            url = self.url.format(name,i)
            self.get_html(url)

if __name__ == '__main__':
    spider = BaiDu()
    spider.run()
