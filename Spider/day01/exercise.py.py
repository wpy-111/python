"""
   爬猫眼电影
"""
from urllib import request,parse
import re
import time
import random
class Maoyan():
    def __init__(self):
        self.url = "https://trade.maoyan.com/board/4?offset={}"
        self.header={'User-Agent':"Win7:Mozilla/5.0 "
                      "(Windows NT 6.1; WOW64) AppleWebKit/535.1"
                      " (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}


    def get_html(self,url):
        req = request.Request(url=url, headers=self.header)
        res = request.urlopen(req)
        html = res.read().decode()
        return html
    def dispose_html(self,html):
        rs ="""
        <a href=.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?上映时间：(.*?)</p>    </div>
            """
        pattern = re.compile(rs,re.S)
        r = pattern.findall(html)
        return r
    def run(self):
        for item in range(0,10):
            page = (item-1) * 10
            url = self.url.format(page)
            html = self.get_html(url)
            r=self.dispose_html(html)
            print("第%d页抓取成功"%item)
            print(r)
            time.sleep(random.randint(1,2))
if __name__ == '__main__':
    s = Maoyan()
    s.run()