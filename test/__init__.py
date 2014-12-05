#-*- coding:utf-8 -*-

class RedisKey(object):
	def __init__(self,redis):
		self.redis = redis

	def __getattr__(self,attr):
		def _(name=''):
			return self(attr,name)
		return _

	def __call__(self,attr,name=''):
		key = attr+name
		redis = self.redis


REDIS_CONFIG = dict(
	host = '192.168.1.109',
	port = 22122,
	db = 0,
	#socket_connect_timeout = 10,
	)

from redis import StrictRedis
redis = StrictRedis(**REDIS_CONFIG)
redis_key = RedisKey(redis)

REDIS_APP_IDENTIFY = redis_key.AppIdentify('%s-%s')
print REDIS_APP_IDENTIFY

