# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #一级页面 大类标题，url 小类的名字 url
    parent_name = scrapy.Field()
    parent_url = scrapy.Field()
    son_name = scrapy.Field()
    son_url = scrapy.Field()
    #二级页面 新闻的链接
    news_url = scrapy.Field()
    #三级页面 新闻的标题和内容
    news_head = scrapy.Field()
    news_content = scrapy.Field()
    #路径：。/data/体育/NBA/
    son_directory = scrapy.Field()