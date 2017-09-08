# -*- coding: utf-8 -*-

import pymysql
import json
class ItcastPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', 'root', 'test')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        json_str = json.dumps(item)
        # item_dict = json.loads(json_str)
        # print(item_dict)
        sql = "insert into itcast(image_url, title) values(item_dict.image_url, item_dict.title)"
        # sql = "insert into itcast(image_url, title) values(item_dict['image_url'], item_dict['title'])"
        self.cursor.execute(sql)
        return item
    def close_spider(self, item, spider):
        self.conn.close()





