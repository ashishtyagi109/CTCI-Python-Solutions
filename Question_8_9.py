def parens(n):
	curStr = ""
	parensHelper(curStr, n, n)

def parensHelper(curStr, openRem, closeRem):
	if ((openRem == 0) and (closeRem == 0)):
		print curStr
	else:
		if (openRem < closeRem):
			curStr += ')'
			parensHelper(curStr, openRem, closeRem - 1)
			curStr = curStr[:-1]
		if (openRem > 0):
			curStr += '('
			parensHelper(curStr, openRem - 1, closeRem)

def main():
	input = int(raw_input('Enter number of parens: '))
	parens(input)

if __name__ == '__main__':
	main()