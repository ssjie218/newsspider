# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 电影实体类
class NewsItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 链接
    link = scrapy.Field()
    # UUID
    uuid=scrapy.Field()
    # 创建时间
    createTime =scrapy.Field()
