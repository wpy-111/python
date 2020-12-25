# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .settings import *
import pymysql
class TencentPipline(object):
    def process_item(self, item, spider):
        print(item)
        return item

class TencentMysqlPipeline:
    def open_spider(self, spider):
        """爬虫项目启动时,连接数据库1次"""
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset=CHARSET)
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        ins = 'insert into tencenttab values(%s,%s,%s,%s,%s,%s)'
        list = [
            item['job_name'],
            item['job_type'],
            item['job_duty'],
            item['job_require'],
            item['job_address'],
            item['job_time']
        ]
        self.cursor.execute(ins, list)
        self.db.commit()
        return item

    def close_spider(self, spider):
        """爬虫项目结束时,断开数据库1次"""
        self.cursor.close()
        self.db.close()
