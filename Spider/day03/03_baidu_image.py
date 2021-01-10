"""
   抓取百度首页30张照片，保存到/home/tarena/imagine/关键字/xxx
"""
from urllib import parse
import requests
import re
import time
import random
import os

class BaiduImage:
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        self.headers = {'User-Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
        #用于命名
        self.i = 1
        self.word = input("请输入关键字:")
        self.directory = '/home/tarena/image/{}/'.format(self.word)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def get_image(self):
        #1.拼接url地址
        params = parse.quote(self.word)
        url =self.url.format(params)
        html = requests.get(url=url,headers=self.headers).text
        #2.正则解析提取图片链接
        regex = '"thumbURL":"(.*?)"'
        pattern = re.compile(regex,re.S)
        src_list = pattern.findall(html)
        #src_list = ['','','']
        for src in src_list:
            self.save_image(src)
            time.sleep(random.uniform(0,1))
    def save_image(self,src):
        #保存一张图片
        html = requests.get(url=src,headers=self.headers).content
        filename = '{}{}{}.jpg'.format(self.directory,self.word,self.i)
        with open(filename,'wb')as f:
            f.write(html)
        self.i += 1
        print(filename,"下载成功")
    def run(self):
        self.get_image()
if __name__ == '__main__':
    r = BaiduImage()
    r.run()
