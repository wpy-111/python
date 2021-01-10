import scrapy


class SouSpider(scrapy.Spider):
    name = 'sou'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        #response直接调用xpath，结果为列表
        r_list = response.xpath('/html/head/title/text()').extract()
        print('*'*50)
        print(r_list)
        print('*'*50)






