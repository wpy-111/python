# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.media import MediaPipeline
class SoPipeline(ImagesPipeline):
    #把图片链接交给调度器
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img_url'],meta={'meta1':item})

    # 重写file_path方法，处理文件名的问题
    # def file_path(self, request, response=None, info=None, *, item=None):
    #     #请求对象requests中，所有属性为Requests()中的参数
    #     #比如 requests.url requests.meta
    #     #把title中不能作为文件名的特殊字符
    #     all_chars ='/\|*?<>"'
    #     title = request.meta['meta1']['img_title']
    #     print(title)
    #     for char in title:
    #         if char in all_chars:
    #             title = title.replace(char,'')
    #
    #     filename = title + '.' +request.url.split('.')[-1]
    #     return filename








