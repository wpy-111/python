import scrapy
from ..items import *

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        url = 'https://maoyan.com/board/4?offset={}'
        for i in range(0,91,10):
            page_url = url.format(i)
            yield scrapy.Request(url=page_url,callback=self.parse)
    def parse(self, response):
        item = MaoyanItem()
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').get()
            item['star'] = dd.xpath('./div/div/div/p[@class="star"]').get()
            item['time'] = dd.xpath('./div/div/div/p[@class="releasetime"]').get()
            yield item