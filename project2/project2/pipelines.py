# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import asyncio
import aiofile
from pymongo import MongoClient

class Project2Pipeline:

    def __init__(self):
        super(Project2Pipeline, self).__init__()
        con = MongoClient('127.0.0.1', 27017)
        db = con['job51']
        self.collection = db['jobinfos']

    def process_item(self, item, spider):
        data = {
            'title': item['title'],
            'company': item['company'],
            'addr': item['addr'],
            'salary': item['salary']
        }
        self.collection.insert(data)
        return item



