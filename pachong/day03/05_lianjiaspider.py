"""
   lxml+xpath 提取链家二手房的信息
"""
import requests
from lxml import etree
import random
import time
from fake_useragent import UserAgent
class LianJiaSpider:
    def __init__(self):
        self.url = 'https://ty.lianjia.com/ershoufang/pg{}/'

    def get_html(self,url,headers):
        """爬虫函数"""
        #遇到未相应页面，尝试三次
        for i in range(3):
            try:
                html = requests.get(url=url,headers=headers,timeout=3).text
                self.parese_html(html)
                break
            except Exception as e:
                print('Retry')
    def parese_html(self,html):
        """解析html"""
        p = etree.HTML(html)
        #先写基准的xpath表达式，然后再for循环一次遍历
        #节点对象
        li_list = p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        item = {}
        for li in li_list:
            name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')

            item['name'] = name_list[0].strip() if name_list else None
            add_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')

            item['address'] = add_list[0].strip() if name_list else None
            hinfo_list = li.xpath('.//div[@class="houseInfo"]/text()')
            if len(hinfo_list) == 7:
                hinfo_list = hinfo_list[0].split('|')
                item['model'] = hinfo_list[0]
                item['area'] = hinfo_list[1]
                item['direct'] = hinfo_list[2]
                item['perfect'] = hinfo_list[3]
                item['floor'] = hinfo_list[4]
                item['year'] = hinfo_list[5]
                item['type'] = hinfo_list[6]

            else:
                item['model'] = None
                item['area'] = None
                item['direct'] = None
                item['perfect'] = None
                item['floor'] = None
                item['year'] = None
                item['type'] = None
            total_list = li.xpath('.//div[@class="totalPrice"]/span/text()')
            print(total_list)
            item['total'] = total_list[0].strip() if total_list else None
            unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
            print(unit_list)
            item['unit'] = unit_list[0].strip() if unit_list else None
            print(item)
    def run(self):
          for page in range(1,100):
              url = self.url.format(page)
              headers = {'User-Agent':UserAgent().random}
              self.get_html(url,headers)
              time.sleep(random.uniform(0,2))

if __name__ == '__main__':
    spider = LianJiaSpider()
    spider.run()











