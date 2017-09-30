# getproxy_tool
getproxy脚本


安装： 
$ pip install -U getproxy

运行py脚本 
$ python /usr/bin/get_proxies_to_redis.py

# -*- coding:utf-8 -*-
# get_proxies_to_redis.py

import redis
from getproxy import GetProxy

g = GetProxy()

g.init()
g.load_plugins()
g.grab_web_proxies()
g.validate_web_proxies()

if g.valid_proxies:

	rds = redis.Redis('10.180.55.40', port=6379, password='demo')
	# 删除key->更新全部代理地址
	rds.delete('ips')

	for i in g.valid_proxies:
		if i['anonymity'] == 'high_anonymous':
			proxy_url = ''.join([i['type'], '://', i['host'], ':', str(i['port'])])
			rds.sadd('ips', proxy_url)
			print 'saved:',proxy_url
参考：https://github.com/fate0/getproxy
