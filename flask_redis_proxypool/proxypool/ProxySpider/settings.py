#!usr/bin/env python
#-*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2019/1/11 21:32

# 代理池数量界限
POOL_UPPER_THRESHOLD = 350

# 检查周期
TESTER_CYCLE = 2
# 获取周期
GETTER_CYCLE = 2

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10

VALID_STATUS_CODES = [200, 302]