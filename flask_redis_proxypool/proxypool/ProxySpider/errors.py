#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2019/1/11 21:25

class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')