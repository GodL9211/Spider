#!usr/bin/env python
# -*- coding:utf-8 _*-
# __author__：连海峰
# __time__：2018/10/21 21:22
"""
希望爬取的信息有排名、片名、电影图片、主演、发布时间、评分
"""
import json
import os
import re
import sys

import requests
import socket
import urllib.error

sys.path.append(os.path.abspath(os.getcwd()))

from requests_deractor import httperror_deractor

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'cache-control': 'max-age=0',
    'authority': 'maoyan.com',
    'cookie': '__mta=53827095.1540126925646.1540129921203.1540135079301.10; uuid_n_v=v1; uuid=8118CC80D53111E8838619F720823F01CA6297ABB4E44CD9AB1AB068D15D03D1; _csrf=b44fd5aaa6eb617d85b4cdcd41d3839067c69f88e3fcae6b5f9ea13f5db8bdda; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=16696b7e2abc8-0203b364514073-e323462-1fa400-16696b7e2abc8; _lxsdk=8118CC80D53111E8838619F720823F01CA6297ABB4E44CD9AB1AB068D15D03D1; __mta=53827095.1540126925646.1540126925646.1540126945766.2; _lxsdk_s=16697344d79-479-f7e-830%7C%7C2',
}


@httperror_deractor
def get_one_page(url, offset):
    response = requests.get(url, headers=headers, timeout=20, params=offset)
    if response.status_code == requests.codes.ok:
        return response.text


def parse_one_page(html):
    print("begin parse")
    # regex = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title.*?>(.*?)<.*?star">(.*?)<.*?releasetime">(.*?)<.*?score">.*?>(.*?)<.*?fraction">(.*?)<.*?dd>'
    regex = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
    pattern = re.compile(regex, re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            "index": item[0],
            "image_url": item[1],
            "title": item[2],
            "actor": item[3].strip(),
            "time": item[4].strip()[5:] if len(item[4]) > 5 else "",
            "score": item[5].strip() + item[6].strip()
        }


def write_to_file(content):
    with open(os.path.join(os.path.abspath(os.getcwd()) + os.path.sep, "maoyan.txt"), "a", encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + os.linesep.strip("\r"))


def main():
    url = "https://maoyan.com/board/4"
    for i in range(10):
        offset = {
            "offset": str(10 * i)
        }
        html = get_one_page(url, offset)
        if html:
            items = parse_one_page(html)
            for item in items:
                write_to_file(item)


if __name__ == '__main__':
    main()
