import numpy

def permCheck(str1, str2):
	map = {}
	for c in str1:
		if c in map:
			map[c] += 1
		else:
			map[c] = 1

	for c in str2:
		if c not in map:
			return False
		if map[c] > 0:
			map[c] -= 1
		else:
			return False

	for key, value in map.iteritems():
		if value != 0:
			return False
	return True

str1 = raw_input("Enter String 1: ")
str2 = raw_input("Enter String 2: ")
print permCheck(str1, str2)