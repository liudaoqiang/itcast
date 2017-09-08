# -*- coding: utf-8 -*-
import scrapy
from itcast.items import ItcastItem

class ItcastSpiderSpider(scrapy.Spider):
    name = 'itcast_spider'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        node_list = response.xpath("//li[@class='a_gd']")
        for index, node in enumerate(node_list):
            item = ItcastItem()
            image_url = node.xpath("p[@class='img_box']/a/img/@src").extract()
            title = node.xpath("p/a[@se_prerender_url='complete']/text()").extract()

            if(len(image_url) > 0):
                item['image_url'] = image_url[0]
                if(len(title) > 0):
                    item['title'] = title[0]
                else:
                    item['title'] = ''
                yield item
        pass
