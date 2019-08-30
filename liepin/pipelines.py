# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class LiepinPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDbPipeline(object):
    collections='task'

    def __init__(self,url,db):
        self.url=url
        self.db=db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            url=crawler.settings.get('MONGO_URI'),
            db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.url)
        self.mdb=self.client[self.db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        if not item['job']:
            return item
        data={
            'job_name':item['job'].strip()
        }
        table=self.mdb[self.collections]
        table.insert_one(data)
        return item

