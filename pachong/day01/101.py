from urllib import request,parse
from time import sleep
from random import randint
class BaiduSpider:
    def __init__(self):
        """定义常用变量"""
        self.url='https://scrm.vivo.com.cn/scrm-fans-activity/#/index?wechatConfigId=92&id=247112931672593472'
        self.header={'User_Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
    #请求函数 - 获取html
    def get_html(self,url):
        req=request.Request(url=url,headers=self.header)
        res=request.urlopen(req)
        html=res.read().decode()
        return html
    #解析提取数据  -提取具体数据
    def parse_html(self):
        pass
    # 保存数据
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    #程序入口函数
    def run(self):
        for item in range(0,10):
            url = self.url
            self.get_html(url)
            print("第%d页抓取成功"%item)
            sleep(randint(1,2))
if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()