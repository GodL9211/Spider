#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：连海峰
# __time__：2018/12/5 23:42
import os

basedir = os.path.realpath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY = os.environ.get("SECRET_KEY", "23dsds3fdhhhncvmdgfd")
    SERVER_NAME = os.environ.get("SERVER_NAME", "127.0.0.1:19003")
    DEBUG = os.environ.get("DEBUG", "False")

class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

config = {
    "development_config": DevelopmentConfig,
    "production_config": ProductionConfig,
}

TEMPLATE_PATH = os.path.join(basedir, "templates")