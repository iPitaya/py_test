# -*-coding:utf-8 -*-
import functools
from statsd import StatsClient

def des1(prefix):
	def _des1(func):
		@functools.wraps(func)
		def __des1():
			print func.__name__,prefix
			return func()
		'''
		@functools.wraps(func)
		def __des1(*args,**kw):
			print func.__name__,prefix
			#return func(*args,**kw)
			return func()
		'''
		return __des1
	return _des1

def des2(prefix):
	def _des2(func):
		@functools.wraps(func)
		def __des2():
			print func.__name__,prefix
			return func()
		return __des2
	return _des2

@des1('des1')
@des2('des2')
def test():
	print  'test'

test()
statsd = StatsClient('192.168.1.89')
print statsd
