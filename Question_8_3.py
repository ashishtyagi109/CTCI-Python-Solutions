# Assuming values in array are not distinct
def magicIndex(arr):
	if arr is None:
		return -1
	return getIndex(arr, 0, len(arr))

def getIndex(arr, low, high):
	if (high <= low):
		return -1

	midIndex = (low + high)/2
	midValue = arr[midIndex]

	if (midIndex == midValue):
		return midIndex

	leftIndex = min(midIndex, midValue)
	left = getIndex(arr, low, leftIndex)
	if (left >= 0):
		return left

	rightIndex = max(midIndex + 1, midValue)
	right = getIndex(arr, rightIndex, high)
	return right