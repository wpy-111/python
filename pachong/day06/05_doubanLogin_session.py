"""
    使用requests 的session类，作会话保持
"""
import requests
from fake_useragent import UserAgent
class DouBanLogin:
    def __init__(self):
        #post_url 用来登录豆瓣
        self.url = 'https://accounts.douban.com/j/mobile/login/basic'
        self.data = {'ck':'' ,
                    'remember':'true',
                    'name':'15834383659',
                    'password':'wpy807807',
                    }
        self.headers = {'User-Agent':UserAgent().random}
        #需要抓取的个人主页的地址
        self.get_url = 'https://www.douban.com/people/227501211/'
        self.s = requests.session()
    def login(self):
        #登录豆瓣发送post请求
        x = self.s.post(url=self.url,headers=self.headers,data=self.data).json()
        print(x)
        html = self.s.get(url=self.get_url,headers = self.headers).text
        print(html)

if __name__ == '__main__':
    spider =DouBanLogin()
    spider.login()










































