"""
  selenium切换句柄
  抓取民政部网站最新行政区划分代码
"""
from selenium import webdriver
import time
class GovSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.options =webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)

    def parse_html(self):
        #1.找最新的链接的节点
        self.browser.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[1]/td[2]/a').click()

        #2.切换句柄到最新的页面  all-handles->列表[handle1,handle2]
        all_handles = self.browser.window_handles
        self.browser.switch_to.window(all_handles[1])
        #3.数据提取
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(name,":",code)
        self.browser.quit()

if __name__ == '__main__':
    spider = GovSpider()
    spider.parse_html()










