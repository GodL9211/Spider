#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：连海峰
# __time__：2018/10/21 23:24
import os
import sys
sys.path.append(os.path.abspath(os.getcwd()))

def httperror_deractor(func):
    def wrap(*args, **kwargs):
        try:
            return func(*args)
        except Exception as e:
            raise Exception(repr(e))
    return wrap

if __name__ == '__main__':
    pass