# -*- coding :utf8 -*-

class locker:
	def __init__(self):
		print "locker.__init__()"

	@staticmethod
	def acquire():
		print "locker.acquire called."

	@staticmethod
	def release():
		print "locker.release()"

def deco(cls):
	def _deco(func):
		def __deco():
			print "before %s called [%s]." % (func.__name__,cls)
			cls.acquire()
			try:
				return func()
			finally:
				cls.release()
		return __deco
	return _deco

@deco(locker)
def myfunc():
	print "myfunc() called"

myfunc()
myfunc()

