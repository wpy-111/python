import scrapy
from ..items import BaiduItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        item = BaiduItem()
        item['title'] = response.xpath('/html/head/title/text()').get()
        print('看不见你的笑，我睡得着')
        yield item

