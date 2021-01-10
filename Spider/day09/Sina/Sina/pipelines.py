# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SinaPipeline:
    def process_item(self, item, spider):
        dir = item['son_directory']+'/'+item['news_head']+'.text'
        with open(dir,'w',encoding='utf-8',errors='ignore')as f:
            f.write(item['news_content'])
        f.close()
        return item
