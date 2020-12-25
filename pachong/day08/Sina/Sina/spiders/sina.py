import scrapy
from ..items import *
import os
class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        #用来存放下一次交给调度器的所有Request -- 所有小分类的请求
        items = []
        div_list = response.xpath('//div[@class="section"]/div')
        for div in div_list:
            parent_name = div.xpath('./h3/a/text()').get()
            parent_url = div.xpath('./h3/a/@href').get()
            #小分类的li节点对象列表
            li_list = div.xpath('./ul/li')
            #有的 特殊大分类get（）出来的None，
            if parent_name and parent_url:
                for li in li_list:
                    item = SinaItem()
                    item['son_name'] = li.xpath('./a/text()').get()
                    item['son_url'] = li.xpath('./a/@href').get()
                    item['parent_name'] = parent_name
                    item['parent_url'] = parent_url
                    son_directory = './data/{}/{}'.format(item['parent_name'],item['son_name'])
                    item['son_directory'] = son_directory
                    #创建对应的目录结构
                    if not os.path.exists(item['son_directory']):
                        os.makedirs(item['son_directory'])
                    items.append(item)
        #大循环结束，items存放了所有的小分类item对象
        #交给调度器
        for item in items:
            yield scrapy.Request(url=item['son_url'],meta={'meta':item},callback=self.detail_parse)


    def detail_parse(self,response):
        meta_item = response.meta['meta']
        items = []
        #t通过观察url规律，新闻链接j基本上以大分类的url开头，以.shtml结尾
        news_url_list = response.xpath('//a/@href').extract()
        for news_url in news_url_list:
            if news_url.startswith(meta_item['parent_url']) and news_url.endswith('.shtml'):
                #只要把url对象交给调度器入队列，说明你创建item对象的时候到了
                item = SinaItem()
                item['news_url'] = news_url
                item['parent_name'] = meta_item['parent_name']
                item['parent_url'] = meta_item['parent_url']
                item['son_name'] = meta_item['son_name']
                item['son_url'] = meta_item['son_url']
                item['son_directory'] = meta_item['son_directory']
                items.append(item)

        for item in items:
            yield scrapy.Request(url=item['news_url'],meta={'meta2':item},callback=self.get_connect)


    def get_connect(self,response):
        item = response.meta['meta2']
        item['news_head'] = response.xpath('//h1[@class="main-title"]/text()').get()
        content = response.xpath('//div[@class="article"]/p/text()').extract()
        item['news_content'] = '\n'.join(content)
        yield item
