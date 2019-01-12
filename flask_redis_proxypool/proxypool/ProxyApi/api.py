#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2019/1/10 21:49
from flask import Flask, g
import sys
sys.path.insert(0, "..")
# print(sys.path)
# print(__name__)
from ProxyApi import create_app
from DB.RedisClient import RedisClient
from DB.db_settings import REDIS_KEY
from flask import render_template
# print("*"*29)
print(__name__)
__all__ = ['app']
app = create_app(App=__name__)
# app = Flask(__name__)

def get_conn():
    print(g)
    print("g is ----")
    if not hasattr(g, "redis"):
        g.redis = RedisClient(REDIS_KEY)
    return g.redis

@app.route("/")
def index():
    return "<h2>Welcome to Proxy Pool System</h2>"

@app.route("/random")
def get_proxy():
    """
    get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    if conn.random() == None:
        return "Redis中没有proxy"
    # return conn.random()
    return render_template("index.html", proxy=conn.random())

@app.route("/count")
def get_counts():
    """
    get the count of proxies
    :return: 总代理数
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == "__main__":
    print("@"*20)
    app.run()
