def permWithDups(freqTable):
	permutations = []

	flag = True

	for key, value in freqTable.iteritems():
		if value > 0:
			flag = False
			freqTable[key] -= 1
			partials = permWithDups(freqTable)
			for word in partials:
				permutations.append(key + word)
			freqTable[key] += 1

	if flag: # all values in map were 0, add empty string to permutations
		permutations.append("")
	return permutations

def generateFreqTable(string):
	freqTable = {}
	for char in string:
		if char in freqTable:
			freqTable[char] += 1
		else:
			freqTable[char] = 1
	return freqTable

def main():
	string = raw_input('Enter string with duplicate characters: ')
	freqTable = generateFreqTable(string)
	print '\nIts permutations are: '
	print permWithDups(freqTable)

if __name__ == '__main__':
	main()
