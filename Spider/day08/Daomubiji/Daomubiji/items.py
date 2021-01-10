# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomubijiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #一级页面 抓取主题和链接
    theme = scrapy.Field()
    theme_url = scrapy.Field()
    #二级页面抓取 题目和链接
    title =scrapy.Field()
    title_url = scrapy.Field()
    #三级页面抓取 内容
    content = scrapy.Field()
    directory = scrapy.Field()
