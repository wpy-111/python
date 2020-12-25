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
        items = []
        for li in li_list:
            #每辆汽车的请求对象
            item = GuaziItem()
            item['url'] = 'https://www.guazi.com'+li.xpath('./a/@href').extract()[0]
            item['name'] = li.xpath('./a/@title').extract()[0]
            item['price'] = li.xpath('./a/div[@class="t-price"]/p/text()').extract()[0]
            items.append(item)
        for item in items:
            #Request中meta参数：在不同解析函数之间传递数据，item数据会随着response一起
            yield scrapy.Request(url=item['url'],meta={'item':item},callback=self.detail_parse)

    def detail_parse(self,response):
        item = response.meta['item']
        item['time'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[1]/span').get()
        item['km'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[2]/span').get()
        item['disp'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[3]/span').get()
        item['trans'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[4]/span').get()
        yield item




