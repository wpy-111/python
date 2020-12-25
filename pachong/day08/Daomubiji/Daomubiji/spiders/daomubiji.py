import scrapy
from  ..items import DaomubijiItem
import os
class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        items = []
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a ')
        for a in a_list:
            item = DaomubijiItem()
            item['theme'] = a.xpath('./text()').get()
            item['theme_url'] = a.xpath('./@href').get()
            items.append(item)
        for one in items:
            yield scrapy.Request(url=one['theme_url'],meta={'meta1':one},callback=self.parse_one)


    def parse_one(self,response):
        meta1 = response.meta['meta1']
        items = []
        article_list = response.xpath('//article')
        for article in article_list:
            item = DaomubijiItem()
            item['title'] = article.xpath('./a/text()').get()
            item['title_url'] = article.xpath('./a/@href').get()
            item['theme'] = meta1['theme']
            item['theme_url'] = meta1['theme_url']
            item['directory'] = './data/{}'.format(item['theme'])
            try:
                if not os.path.exists(item['directory']):
                    os.makedirs(item['directory'])
            except Exception as e:
                print(e)
            items.append(item)
        for two in items:
            yield scrapy.Request(url=two['title_url'],meta={'meta2':two},callback=self.parse_two)

    def parse_two(self,response):
        item = response.meta['meta2']
        content_list = response.xpath('//article[@class="article-content"]/p/text()').extract()
        item['content'] = '\n'.join(content_list)
        yield item



