import scrapy
from urllib import parse
import requests
import json
from ..items import TencentItem
from scrapy_redis.spiders import RedisSpider
class TencentSpider(RedisSpider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1607861793019&postId={}&language=zh-cn'
    keyword = input("请输入职位类别:")
    keyword = parse.quote(keyword)
    #分布式配置 redis_key
    #1.去掉redis_urls
    #2.定义redis_key
    # start_urls = [one_url.format(keyword,1)]
    redis_key = 'tencent:spider'
    def get_total(self):
        url = self.one_url.format(self.keyword,1)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',}
        html = requests.get(url=url,headers=headers).json()
        count = html['Data']['Count']
        total = count//10 if count%10==0 else count//10+1
        return total
    #重写start_requests()方法
    def parse(self,response):
        """把所有一级页面的url地址入队列"""
        total = self.get_total()
        for index in range(1,total+1):
            url = self.one_url.format(self.keyword,index)
            yield scrapy.Request(url=url,callback=self.parse_one_page)
    def parse_one_page(self,response):
        """一级页面解析函数"""
        #转为python数据类型
        html = json.loads(response.text)
        for one in html['Data']['Posts']:
            item = TencentItem()
            item['post_id'] = one['PostId']
            item['job_url'] = self.two_url.format(item['post_id'])
            yield scrapy.Request(url=item['job_url'],meta={'meta1':item},callback=self.parse_two_page)
    def parse_two_page(self,response):
        item = response.meta['meta1']
        html = json.loads(response.text)
        item['job_name'] = html['Data']['RecruitPostName']
        item['job_type'] = html['Data']['CategoryName']
        item['job_duty'] = html['Data']['Responsibility']
        item['job_require'] = html['Data']['Requirement']
        item['job_address'] = html['Data']['LocationName']
        item['job_time'] = html['Data']['LastUpdateTime']
        yield item




