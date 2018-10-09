# encoding: utf-8
'''
@author: shen
@file: NewsSpider.py
@time: 2018/08/06
@Software: PyCharm
@desc:
'''
import re

from scrapy import Request
from scrapy.spiders import Spider
from news_spider.items import NewsItem
import datetime
import time
import uuid
class NewsSpider(Spider):
    name = 'news_spider'

    def start_requests(self):
        url = 'http://finance.ifeng.com/'
        yield Request(url)

    def parse2(self, response):
        item2 =NewsItem()
        item = response.meta;
        content =response.xpath('//div[@id="artical"]')
        #http://finance.ifeng.com/a/20180806/16429540_0.shtml
        if  'finance.ifeng.com/a' not in item['link'] or '.shtml' not in item['link'] :
            return
        # 时间  判断20分钟内的新闻不保存
        publishTime=content[0].xpath('.//span[@itemprop="datePublished"]/text()').extract_first()
        if publishTime < ((datetime.datetime.now() - datetime.timedelta(minutes=19)).strftime('%Y-%m-%d %H:%M:%S')):
           return
        item2["createTime"]=publishTime;
        #title, artical, origin, link
        # 来源
        origin = content[0].xpath('.//span[@itemprop="publisher"]/span/a/text()').extract_first()
        if origin is None:
            origin = content[0].xpath('.//span[@itemprop="publisher"]/span/text()').extract_first()
        item2["source"] = origin
        #标题
        title = content[0].xpath('.//h1[@itemprop="headline"]/text()').extract_first()
        item2["title"]=title
        #内容
        artical = content[0].xpath('.//div[@id="artical_real"]').xpath('string(.)').extract_first()
        item2["content"]=artical.replace('\r\n', '').replace(' ', '').replace('\n', '')[0:200]
        item2["link"]=item["link"]
        item2["uuid"] = uuid.uuid1()
        yield item2



    def parse(self, response):
        item = NewsItem()
        movieList = response.xpath('//div[@class="col01L"]/div[@class="box_02"]/ul/li')
        for movie in movieList:
            link =movie.xpath('.//a/@href').extract_first()
            item["link"]=link
            yield Request(link,callback=self.parse2,meta=item)

