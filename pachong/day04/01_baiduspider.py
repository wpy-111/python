import requests
import os
import time
import random
from lxml import etree
from urllib import parse

class TieBaImagine:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    def get_html(self,url):
        html = requests.get(url=url,headers=self.headers).text
        return html
    def xpath_func(self,html,xbds):
        p = etree.HTML(html)
        r_list = p.xpath(xbds)
        return r_list

    def parse_html(self,one_url):
        one_html = self.get_html(one_url)
        one_xpath = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        href_list = self.xpath_func(one_html,one_xpath)
        for href in href_list:
            t_link = 'http://tieba.baidu.com'+href
            self.save_image(t_link)
    def save_image(self,t_link):
        two_html = self.get_html(t_link)
        two_xpath = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        image_link_list = self.xpath_func(two_html,two_xpath)
        for  img_link in image_link_list:
            self.save_one_img(img_link)
            time.sleep(random.uniform(0,1))
    def save_one_img(self,img_link):
        img_html = requests.get(url=img_link,headers=self.headers).content
        directory = '/home/tarena/baidu'
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = '/home/tarena/baidu/'+img_link[-10:]
        with open(filename,'wb')as f:
            f.write(img_html)
        print(filename,"下载成功")
    def run(self):
        name = input("请输入贴吧名：")
        start_page = int(input("请输入起始页："))
        end_page = int(input("请输入结束页："))
        params = parse.quote(name)
        for page in range(start_page,end_page+1):
            pn = (page-1)*50
            url = self.url.format(params,pn)
            self.parse_html(url)
if __name__ == '__main__':
    spider = TieBaImagine()
    spider.run()