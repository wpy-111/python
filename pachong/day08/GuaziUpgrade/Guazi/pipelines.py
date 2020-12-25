# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from .settings import *
class GuaziPipeline(object):
    #item：从爬虫文件中 yield item 过来的这个item对象
    def process_item(self, item, spider):
        #简单打印输出
        print(item['name'],item['price'],item['url'],item['time'],item['km'],item['disp'],item['trans'])
        return item
#管道二：存入mysql数据库
class GuaziMysqlPipline(object):
    def open_spider(self,spider):
        """爬虫项目启动，只执行一次，一般用于数据库的链接 """
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset=CHARSET)
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into guaziset values(%s,%s,%s)'
        car_list = [item['name'],item['price'],item['url']]
        self.cursor.execute(ins,car_list)
        self.db.commit()
        return item

    def close_spider(self,spider):
        """爬虫程序结束时，只执行一次，一般用于数据库的断开"""
        self.cursor.close()
        self.db.close()



