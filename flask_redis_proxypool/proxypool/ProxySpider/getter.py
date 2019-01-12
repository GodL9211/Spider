#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2019/1/11 21:45

from .tester import Tester
from DB.RedisClient import RedisClient
from .crawler import Crawler
from .settings import *
from DB.db_settings import *
import sys


class Getter():
    def __init__(self):
        self.redis = RedisClient(REDIS_KEY)
        self.crawler = Crawler()

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies = self.crawler.get_proxies(callback)
                # sys.stdout.flush()
                for proxy in proxies:
                    self.redis.put(proxy)
        else:
            print("代理池满了，等待抓取代理")
            sys.stdout.flush()