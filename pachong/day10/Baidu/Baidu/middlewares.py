# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class BaiduSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BaiduDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
#中间键一 包装User-Agent
from fake_useragent import UserAgent
class BaiduUaDownloaderMiddleware(object):
    def process_request(self,request,spider):
        #request为被拦截下来的请求对象，利用headers属性设置
        agent = UserAgent().random
        request.headers['User-Agent'] = agent
        print(agent)
#中间键二 包装随机代理IP
from .proxypoor import proxy_list
import random
class BaiduProxyDownloaderMiddleware(object):
    def process_request(self,request,spider):
        #利用meta属性，定义代理
        proxy = random.choice(proxy_list)
        request.meta['proxy'] = proxy
        print(proxy)
    #代理IP不稳定，尝试三次后scrapy会抛出异常
    def process_exception(self,request,exception,spider):
        return request
#中间键三 添加cookie
class BaiduCookieDownloaderMiddleware(object):
    def process_request(self,request,spider):
        #添加cookies：利用request.cookies属性
        cookies_dict = self.get_cookie()
        request.cookies = cookies_dict

    def get_cookie(self):
        cos ='BIDUPSID=3FF71279C5CE63676BA46A7B10B80B8D; PSTM=1601645391; BAIDUID=3FF71279C5CE636751A58C6D0FA02A42:FG=1; BD_UPN=12314753; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1608025338,1608116197; COOKIE_SESSION=259_1_8_5_5_15_0_0_5_6_2506_4_259_1607946338_3_0_1608116421_1607946362_1608116418%7C9%2323_4_1607946359%7C3; BAIDUID_BFESS=4685A09AFBC13B4B092D9B2AC1573A93:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=2; H_PS_645EC=2fc48oyAx%2BmGrAPJjsOCPeTuVJDLK06sTOaoFLa2H%2B5GpTsdyrDzlxAJDk4; H_PS_PSSID=33213_1466_33242_33306_32973_33313_33312_33311_33310_33218_33309_33320_33198_33308_33307_33217_33216_33215; BA_HECTOR=2l20818h852k8k81v11ftrrm20r'
        cookies = {}
        for kv in cos.split('; '):
            cookies[kv.split('=')[0]] = kv.split('=')[1]
        print(cookies)
        return cookies











