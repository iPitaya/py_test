# -*- coding:utf8 -*-

def deco(arg):
	def _deco(func):
		def __deco():
			print "before %s called [%s]." % (func.__name__,arg)
			func()
			print " after %s called [%s]." % (func.__name__,arg)
		return __deco
	return _deco

@deco("mymodule")
def myfunc():
	print " myfunc() called."

@deco("module2")
def myfunc2():
	print "myfunc() called"

myfunc()
myfunc2()
