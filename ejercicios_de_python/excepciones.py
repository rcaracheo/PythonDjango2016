# excepcion
try:
	6/0
except Exception as e:
	print "%s" % e

# superar la excepcion
try:
	7/0
except Exception as e:
	print "%s" % e
	raise e
