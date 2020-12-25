"""
    腾讯招聘指定类别的职位信息抓取 -多线程
"""
import requests
import time
import json
from urllib import parse
from queue import Queue
from fake_useragent import UserAgent
from threading import Thread,Lock

class TencentSpider:
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1606564895725&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId? timestamp=1563912374645&postId={}&language=zh-cn'
        self.one_q = Queue()
        self.two_q = Queue()
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.i = 0

    def get_html(self,url):
        headers = {'User-Agent':'Win7:Mozilla/5.0""(Windows NT 6.1; WOW64) AppleWebKit/535.1"" (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        html = requests.get(url=url,headers=headers)
        return html

    def url_in(self):
        word = input("请输入职位类别：")
        word = parse.quote(word)
        total = self.get_total(word)
        for page in range(1,total+1):
            url = self.one_url.format(word,page)
            self.one_q.put(url)

    def get_total(self,word):
        url = self.one_url.format(word,1)
        html = self.get_html(url=url).json()
        count = int(html['Data']['Count'])
        total = count//10 if count%10==0 else count//10+1
        return total

    def parse_one_page(self):
        """线程一事件函数，获取所有职位的postId的值"""
        while True:
            self.lock1.acquire()
            if not self.one_q.empty():
                one_url = self.one_q.get()
                self.lock1.release()
                html = self.get_html(url=one_url).json()
                for job in html['Data']['Posts']:
                    postId = job['PostId']
                    two_url = self.two_url.format(postId)
                    self.lock2.acquire()
                    self.two_q.put(two_url)
                    self.lock2.release()
            else:
                self.lock1.release()
                break
    def parse_two_page(self):
        while True:
            try:
                self.lock2.acquire()
                two_url = self.two_q.get(block=True,timeout=5)
                print(two_url)
                self.lock2.release()
                html_two = json.loads(self.get_html(two_url))
                item = {}
                item['name'] = html_two['data']['RecruitPostName']
                item['address'] = html_two['data']['LocationName']
                item['type'] = html_two['data']['CategoryName']
                item['time'] = html_two['data']['LastUpdateTime']
                item['duty'] = html_two['data']['Responsibility']
                item['require'] = html_two['data']['Requirement']
                print(item)
                self.lock2.acquire()
                self.i += 1
                self.lock2.release()
            except Exception as e :
                self.lock2.release()
                print(e)
                break
    def run(self):
        self.url_in()
        t1_list = []
        t2_list = []
        for i in range(1):
            t1 = Thread(target=self.parse_one_page)
            t1_list.append(t1)
            t1.start()
        for x in range(1):
            t2 = Thread(target=self.parse_two_page)
            t2_list.append(t2)
            t2.start()
        for n in t1_list:
            n.join()
        for m in t2_list:
            m.join()
        print('职位数量：',self.i)

if __name__ == '__main__':
    start_time = time.time()
    spider = TencentSpider()
    spider.run()
    end_time = time.time()
    print("时间:%.2f"%(end_time-start_time))









