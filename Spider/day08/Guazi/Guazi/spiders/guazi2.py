import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    allowed_domains = ['www.guazi.com']
    #重写start_url   start_requests()方法

    def start_requests(self):
        """生成所有的url地址，一次性交给调度器"""
        for i in range(1,6):
            url = 'https://www.guazi.com/ty/buy/o{}/#bread'.format(i)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        #基准xpath：匹配所有汽车节点对象
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        item = GuaziItem()
        for li in li_list:
            item['url'] = li.xpath('./a/@href').extract()[0]
            item['name'] = li.xpath('./a/@title').extract()[0]
            item['price'] = li.xpath('./a/div[@class="t-price"]/p').extract()[0]
            #把抓取的数据，传递给了管道文件piplines.py
            yield item



