# encoding: utf-8
'''
@author: feizi
@file: test.py
@time: 2017/11/19 17:32
@Software: PyCharm
@desc:
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-




import re
from lxml import etree

import datetime
import time


str = '''
<span itemprop="datePublished" class="ss01">2018-08-06 08:17:26</span>
'''
def beforeTime(date_format='%Y-%m-%d %H:%M:%S'):
    t = time.time() - 20*60
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
    return t

def run():
    briefList = etree.HTML(str ).xpath('.//span[@itemprop="datePublished"]/text()')
    print(briefList[0]);
    print(((datetime.datetime.now() - datetime.timedelta(minutes=20)).strftime('%Y-%m-%d %H:%M:%S')));
    if briefList[0]< ((datetime.datetime.now() - datetime.timedelta(minutes=21)).strftime('%Y-%m-%d %H:%M:%S')):
        print("20分钟内保存");
    else:
        print("超过20分钟不要");
    if "http://finance.ifeng.com/a/20180806/16429300_0.shtml" not in 'finance.ifeng.com':
        print("111");

        print(int(time.time()))
    #if briefList:
        # 以'/'进行分割
        #briefs = re.split(r'/', briefList[1])
        # 上映年份
        #for brief in briefs:
            #if hasNumber(brief):
                #years = ''
                #years = years + re.compile(ur'(\d+)').findall(brief)[0] + ','
                #print years.join(';')

def hasNumber(str):
    return bool(re.search('\d+', str))


if __name__ == '__main__':
    run()