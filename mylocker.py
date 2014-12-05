# -*- coding:utf8 -*-

class mylocker:
	def __init__(self):
		print "mylocker.__init__()"

	@staticmethod
	def acquire():
		print "mylocker.acquire()"

	@staticmethod
	def unlock():
		print   "mylocker.unlock()"

class lockerex(mylocker):
	@staticmethod
	def acquire():
		print "lockerex.acquire()"

	@staticmethod
	def unlock():
		print "locker.unlock()"


def lockhelper(cls):
	def _deco(func):
		def __deco(*args,**kwargs):
			print "before %s called." % func.__name__
			cls.acquire()
			try:
				return func(*args,**kwargs)
			finally:
				cls.unlock()
		return __deco
	return _deco
