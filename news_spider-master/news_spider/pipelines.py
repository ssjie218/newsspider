# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from scrapy.exceptions import DropItem

from news_spider.items import NewsItem

# 获取数据库连接
def getDbConn():
    conn = MySQLdb.Connect(
        host='rm-uf68k7knfx6xhs31k.mysql.rds.aliyuncs.com',
        port=3306,
        user='hhd',
        passwd='jj52ybl7GKXzubDZHzq',
        db='hhd',
        charset='utf8'
    )
    return conn

# 关闭数据库资源
def closeConn(cursor, conn):
    # 关闭游标
    if cursor:
        cursor.close()
    # 关闭数据库连接
    if conn:
        conn.close()


class NewsSpiderPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['title'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['title'])
            if item.__class__ == NewsItem:
                self.insert(item)
                return
        return item

    def insert(self, item):
        try:
            # 获取数据库连接
            conn = getDbConn()
            # 获取游标
            cursor = conn.cursor()
            # 使用 execute()  方法执行 SQL 查询
            sql = "SELECT count(*) from t_information where title=%s "
            params=(item['title'])
            cursor.execute(sql, params)
            # 使用 fetchone() 方法获取单条数据.
            data = cursor.fetchone()
            if(data[0]!=0L):
                return
            # 插入数据库
            share_link='https://hzq.mifang86.com/#/information/'+str(item['uuid']);
            sql = "INSERT INTO t_information(title,content, source, link,share_link,uuid,create_time,modify_time)VALUES(%s, %s, %s,%s, %s,%s,date_sub(str_to_date(%s,'%%Y-%%m-%%d %%H:%%i:%%s'), interval 8 hour),date_sub(now(), interval 8 hour))"
            params = (item['title'], item['content'], item['source'], item['link'],share_link,item['uuid'],item['createTime'])
            cursor.execute(sql, params)
            #事务提交
            conn.commit()
        except Exception, e:
            # 事务回滚
            conn.rollback()
            print 'except:', e
        finally:
            # 关闭游标和数据库连接
            closeConn(cursor, conn)



