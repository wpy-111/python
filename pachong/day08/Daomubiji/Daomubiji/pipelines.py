# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from .items import *

class DaomubijiPipeline:
    def process_item(self, item, spider):
        dir = item['directory']+'/'+item['title'].replace(' ','_')+'.txt'
        try:
            with open(dir,'w',encoding='utf-8',errors='ignore') as f:
                f.write(item['content'])
            f.close()
        except Exception as e:
            print(e)
        return item
