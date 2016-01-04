def pathWithSum(root, targetSum):
	runningSumCount = {}
	runningSum = 0
	return getCounts(root, targetSum, runningSum, runningSumCount)

def getCounts(node, targetSum, runningSum, runningSumCount):
	if node is None:
		return 0

	pathCount = 0
	runningSum += node._value
	if runningSum == targetSum:
		# if current runningSum is equal to targetSum, we'll need to count it
		pathCount += 1

	sum = runningSum - targetSum
	pathCount += runningSumCount.get(sum, 0) # Defaults to 0 if sum not found in map

	if runningSum in runningSumCount:
		runningSumCount[runningSum] += 1
	else:
		runningSumCount[runningSum] = 1
	pathCount += getCounts(node._left, targetSum, runningSum, runningSumCount)
	pathCount += getCounts(node._right, targetSum, runningSum, runningSumCount)
	decrementInMap(runningSumCount, runningSum) # Fix map

	return pathCount

def decrementInMap(map, key):
	map[key] -= 1
	if map[key] == 0:
		del map[key] # Remove runningSum's with frequency 0 to conserve space
