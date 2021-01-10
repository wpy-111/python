"""
   抓取指定贴吧的指定页的数据
"""
from urllib import request,parse
from time import sleep
from random import randint
class BaiduSpider:
    def __init__(self):
        """定义常用变量"""
        self.url='http://tieba.baidu.com/?kw={}&pn={}'
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
        name=input("请输入贴吧名：")
        start_page=int(input("请输入起始页："))
        end_page=int(input("请输入终止页："))
        params = parse.quote(name)
        for item in range(start_page,end_page+1):
            page = (item-1) * 50
            url = self.url.format(params,page)
            html = self.get_html(url)
            filename = "{}_第{}页.html".format(name,item)
            self.save_html(filename,html)
            print("第%d页抓取成功"%item)
            sleep(randint(1,2))
if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()