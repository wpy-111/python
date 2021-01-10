# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #一级页面：链接 价格 名称
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    #二级页面：时间，历程，排量，变速箱
    time = scrapy.Field()
    km = scrapy.Field()
    disp = scrapy.Field()
    trans = scrapy.Field()
#相当于一个字典，{‘url’：‘’，‘name’：‘’，‘price’：‘’}