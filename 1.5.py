def oneAway(str1, str2):
	if(len(str1) == len(str2)):
		return checkForReplace(str1, str2)
	elif (abs(len(str1) - len(str2)) >1):
		return False
	else:
		if(len(str1) > len(str2)):
			return checkForInsRem(str1, str2)
		else:
			return checkForInsRem(str2, str1)

def checkForReplace(str1, str2):
	i = 0
	oneAway = False

	for i in xrange(len(str1)):
		if(str1[i] != str2[i]):
			if oneAway:
				return False
			else:
				oneAway = True
	return True

def checkForInsRem(bigger, smaller):
	i = 0
	j = 0
	oneAway = False

	while(i < len(bigger) and j < len(smaller)):
		if(bigger[i] != smaller[j]):
			if oneAway:
				return False
			else:
				i += 1
				oneAway = True
		else:
			i += 1
			j += 1
	return True

str1  = raw_input('Enter String 1: ')
str2  = raw_input('Enter String 2: ')
print (oneAway(str1, str2))
