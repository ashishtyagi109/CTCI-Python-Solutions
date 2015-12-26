# Assume extended ASCII characters
import numpy
def palPerm(str):
	table  = numpy.zeros(256)

	for c in str:
		if c != ' ':
			table[ord(c.lower())] += 1

	oddFlag = False

	for i in xrange(256):
		if(table[i]%2 != 0):
			if oddFlag:
				return False
			else:
				oddFlag = True
	return True

input = raw_input('Enter String: ')
print palPerm(input)