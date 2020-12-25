import scrapy
from ..items import PptItem

class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.1ppt.com']
    start_urls = ['http://www.1ppt.com/xiazai/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="col_nav clearfix"]/ul/li/a ')
        for li in li_list:
            item = PptItem()
            item['parent_title'] = li.xpath('./text()').get()
            item['parent_url'] = li.xpath('./@href').get()
            url = 'http://www.1ppt.com/'+item['parent_url']
            yield scrapy.Request(url=url,meta={'meta1':item},callback=self.parse_two)

    def get_total(self, response):
        li_list = response.xpath('//div[@class="clearfix"]/ul/li')
        for li in li_list:
            if li.xpath('./a/text()').get() == '末页':
                content = li.xpath('./a/@href').get()
                text = content.split('.')[0]
                total = text.split('_')[-1]
                return int(total)
    def parse_two(self,response):
        meta_item = response.meta['meta1']
        total = self.get_total(response)
        parent_url = meta_item['parent_url']
        if total == None:
            item = PptItem()
            url = 'http://www.1ppt.com'+parent_url+'ppt_'+parent_url.split('/')[-2]+'_1.html'
            item['parent_url'] = url
            item['parent_title'] = meta_item['parent_title']
            yield scrapy.Request(url=item['parent_url'],meta={'meta2':item},callback=self.parse_three)
        else:
            for i in range(1,total+1):
                item = PptItem()
                url = 'http://www.1ppt.com'+parent_url+'ppt_'+parent_url.split('/')[-2]+'_{}.html'.format(i)
                item['parent_url'] = url
                item['parent_title'] = meta_item['parent_title']
                yield scrapy.Request(url=item['parent_url'], meta={'meta2': item}, callback=self.parse_three)

    def parse_three(self,response):
        meta_item = response.meta['meta2']
        li_list = response.xpath('//ul[@class="tplist"]/li')
        for li in li_list:
            item = PptItem()
            son_url = li.xpath('./a/@href').get()
            item['son_url'] = 'http://www.1ppt.com'+son_url
            item['son_title'] = li.xpath('./a/img/@alt').get()
            item['parent_url'] = meta_item['parent_url']
            item['parent_title'] = meta_item['parent_title']
            yield scrapy.Request(url=item['son_url'],meta={'meta3':item},callback=self.parse_four)
    def parse_four(self,response):
        item = response.meta['meta3']
        down_url = response.xpath('//ul[@class="downurllist"]/li/a/@href').get()
        item['down_url'] = 'http://www.1ppt.com' + down_url
        yield item
