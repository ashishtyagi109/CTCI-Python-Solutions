def isSubstring(bigger, smaller):
	return smaller in bigger

def strRotCheck(str1, str2):
	temp = str1+str1
	return len(str1) == len(str2) and isSubstring(temp, str2)

str1 = raw_input('Enter first string: ')
str2 = raw_input('Enter second string: ')

print strRotCheck(str1, str2)