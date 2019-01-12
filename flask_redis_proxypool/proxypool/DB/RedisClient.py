#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2019/1/10 22:30
import random
import redis
import re
import sys
print(sys.path)

from .db_settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, INITIAL_SCORE, MAX_SCORE, MIN_SCORE, REDIS_KEY


class RedisClient(object):
    def __init__(self, name, **kwargs):
        self.db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0)
        self.name = name

    def random(self):
        """
        get one proxy from redis
        :return: one proxy
        """
        keys_list = self.db.zrangebyscore(self.name, MIN_SCORE, MAX_SCORE)
        # print(keys_list)
        return random.choice(keys_list).decode("utf-8") if keys_list else None

    def put(self, proxy, score=INITIAL_SCORE):
        """
        add proxy into redis zset
        :param proxy:
        :param score:
        :return:
        """
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
            print("代理不符合规范", proxy, "舍弃")
            return
        if not self.db.zscore(self.name, proxy):
            return self.db.zadd(self.name, score, proxy)

    def decrease(self, proxy):
        """
        代理值减一分，小于最小值则删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.db.zscore(self.name, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(self.name, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(self.name, proxy)

    def exists(self, proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        return not self.db.zscore(self.name, proxy) == None

    def max(self, proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """
        获取数量
        :return: 数量
        """
        return self.db.zcard(self.name)

    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        return self.db.zrangebyscore(self.name, MIN_SCORE, MAX_SCORE)

    def batch(self, start, stop):
        """
        批量获取
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        return self.db.zrevrange(self.name, start, stop - 1)


if __name__ == '__main__':
    conn = RedisClient(REDIS_KEY)
    result = conn.batch(680, 688)
    print(result)
