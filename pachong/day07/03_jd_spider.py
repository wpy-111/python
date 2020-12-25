"""
   京东商品抓取  -selenium
   selenium中xpath只能获得节点对象不能/text()可以用.text
"""
import time
from selenium import  webdriver
import pymongo
class JDSpider:
    def __init__(self):
        self.url = 'https://www.jd.com/'
        #打开浏览器
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=self.options)
        #mongodb 的常用变量
        self.con = pymongo.MongoClient('localhost',27017)
        self.db = self.con['jddb']
        self.myset =self.db['jdset']

    def get_html(self):
        """打开京东首页，输入内容"""
        self.browser.get(self.url)
        # word = input("请输入关键字：")
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(1)
    def parse_html(self):
        """进习数据提取"""
        #把数据拉到最低，预留加载时间
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        #进行数据的提取基准xpath
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            item = {}
            item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text
            item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text
            item['commit'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text
            item['shop'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text
            print(item)
            self.myset.insert_one(item)
    def run(self):
        self.get_html()
        while True:
            self.parse_html()
            if self.browser.page_source.find('class="pn-next disabled"') == -1:
                self.browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
                time.sleep(1)
            else:
                self.browser.quit()
                break
            #判断是否是最后一页
if __name__ == '__main__':
    spider = JDSpider()
    spider.run()

































