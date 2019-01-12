#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：连海峰
# __time__：2018/12/5 21:37
import os
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

from ProxyApi.settings import config, TEMPLATE_PATH

def create_app(config_name=None, App=None):

    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "development_config")

    app = Flask(App.split(".")[-1], template_folder=TEMPLATE_PATH)
    # app = Flask(App.split(".")[-1], template_folder=r"E:\GitHub\Spider\Spider\flask_redis_proxypool\proxypool\ProxyApi\templates1")
    print("****"*30)

    app.config.from_object(config[config_name])
    print(app.config)
    return app