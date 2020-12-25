import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/ty/buy/o1/#bread']
    n = 1


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
        if self.n < 5:
            self.n += 1
            url = 'https://www.guazi.com/ty/buy/o{}/#bread'.format(self.n)
            #把url地址交给调度器入队列
            yield scrapy.Request(url=url,callback=self.parse)




