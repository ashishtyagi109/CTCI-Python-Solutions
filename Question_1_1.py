import numpy

def unique(str):
	lTable = numpy.zeros((256), dtype=bool)
	for c in str:
		if not lTable[ord(c)]:
			lTable[ord(c)] = True
		else:
			return False
	return True

str = raw_input("Enter String: ")
print unique(str)