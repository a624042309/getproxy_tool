# -*- coding:utf-8 -*-
import redis
from getproxy import GetProxy

g = GetProxy()

g.init()
g.load_plugins()
g.grab_web_proxies()
g.validate_web_proxies()

if g.valid_proxies:

	rds = redis.Redis(host='', port=6379, password='demo')
	# 删除key->更新全部代理地址
	rds.delete('ips')

	for i in g.valid_proxies:
		if i['anonymity'] == 'high_anonymous':
			proxy_url = ''.join([i['type'], '://', i['host'], ':', str(i['port'])])
			rds.sadd('ips', proxy_url)
			print 'saved:',proxy_url