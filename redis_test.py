# -*- coding: utf-8 -*-
from intstr import IntStr

redis_keyer = IntStr(
'!"#$&()+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz{|}~'
)

REDIS_KEY_ID = 'RedisKeyId'
REDIS_KEY = 'RedisKey'
REDIS_ID_KEY = 'RedisIdKey'

_EXIST = set()

class RedisKey(object):
    def __init__(self, redis):
        self.redis = redis

    def __getattr__(self, attr):
	print attr
	print '1'
        def _(name=''):
	    print '---'
            return self(attr, name)
        return _

    def __call__(self, attr, name=''):
	print '2'
        key = attr+name
	print key
        redis = self.redis

        if key in _EXIST:
            print 'REDIS KEY IS ALREADY DEFINED %s !!!'%key


        _EXIST.add(key)
        if redis:
            _key = redis.hget(REDIS_KEY, key)
            if _key is None:
                id = redis.incr(REDIS_KEY_ID)
                _key = redis_keyer.encode(id)
                if name and "%" in name:
                    _key = _key+"'"+name
                p = redis.pipeline(transaction=False)
                p.hset(REDIS_KEY, key, _key)
                p.hset(REDIS_ID_KEY, _key, key)
                p.execute()
            return _key



from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1',port=6379)
redis_test = RedisKey(redis)

print 'start'
REDIS_STAR_COL_COUNT = redis_test.StarCollectCount()
print 'end'
print REDIS_STAR_COL_COUNT

test1 = redis_test.Good()
print test1

test2 = redis_test.Good()
print test2

test_attr = redis_test.test_attr('%s')
print test_attr % 'hh'

redis.hset(REDIS_STAR_COL_COUNT,'good','ok')

result = redis.hget(REDIS_STAR_COL_COUNT,'hello')

print result
rts = redis.hgetall(REDIS_STAR_COL_COUNT)
print rts
id = redis.incr('REDIS_KEY_ID')
kk = redis_keyer.encode(id)
print kk
print id

