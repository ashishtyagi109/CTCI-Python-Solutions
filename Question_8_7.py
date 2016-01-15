def permUnique(curStr, listOfChars):
	if not listOfChars: # listOfChars is empty
		print curStr

	for i in xrange(len(listOfChars)):
		curStr += listOfChars.pop(i)
		permUnique(curStr, listOfChars)
		listOfChars.insert(i, curStr[-1])
		curStr = curStr[:-1]

def main():
	string = raw_input('Enter string with unique characters: ')
	print 'Its permutations are: \n'
	permUnique("", list(string))

if __name__ == '__main__':
	main()
