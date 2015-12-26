from cStringIO import StringIO
def compress(str):
	answer = StringIO()
	if len(str) == 0:
		return str
	lastChar = str[0]
	charCount = 1
	for i in xrange(1, len(str)):
		if str[i] == lastChar:
			charCount += 1
		else:
			answer.write(lastChar)
			if charCount > 1:
				answer.write(`charCount`)
				charCount = 1
			lastChar = str[i]
	answer.write(lastChar)
	if charCount > 1:
		answer.write(`charCount`)
	return answer.getvalue()

input = raw_input('Enter string to compress: ')
print compress(input)
