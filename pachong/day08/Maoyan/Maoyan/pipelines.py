# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['star'],item['time'])
        return item
import pymysql
from .settings import *
class MaoyanMysqlPipline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset=CHARSET)
        self.cur = self.db.cursor()
    def process_item(self,item,spider):
        ins = 'insert into maoyantab values(%s,%s,%s)'
        list = [item['name'],item['star'],item['time']]
        self.cur.execute(ins,list)
        self.db.commit()
        return item
    def close_spider(self,spider):
        self.cur.close()
        self.db.close()
