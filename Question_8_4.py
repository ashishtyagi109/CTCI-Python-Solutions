import copy

def getPowerSet(inputSet):
	if inputSet is None:
		return None
	powerSet = []
	getSubsets(powerSet, inputSet, len(inputSet)-1)
	return powerSet

def getSubsets(powerSet, inputSet, index):
	if (index == -1):
		powerSet.append([])
	else:
		getSubsets(powerSet, inputSet, index - 1)
		subsets = copy.deepcopy(powerSet)
		for key in subsets:
			key.append(inputSet[index])
		powerSet.extend(subsets)

def main():
	setLength = int(raw_input('Enter number of elements in set: '))

	inputSet = []
	for i in xrange(setLength):
		element = raw_input('Enter element {}: '.format(i+1))
		inputSet.append(element)

	print 'Powerset: '
	print getPowerSet(inputSet)

if __name__ == '__main__':
	main()