from numpy import empty

def minTree(sortedArr):
	return minBST(sortedArr, 0, len(sortedArr))

def minBST(sortedArr, start, end):
	if end <= start:
		return None
	mid = (start+end)/2 # Same as (end-start)/2 + start
	node = Node(sortedArr[mid])
	node._left = minBST(sortedArr,start, mid)
	node._right = minBST(sortedArr, mid+1, end)
	return node

class Node:
	def __init__ (self, value, left = None, right = None):
		self._value = value
		self._left = left
		self._right = right

	def __repr__(self):
		return str(self._value)

def inOrder(node):
	if node == None:
		return
	inOrder(node._left)
	print node
	inOrder(node._right)
	
if __name__ == '__main__':
	n = int(raw_input('Enter length of array: '))
	array = empty((n))

	for i in xrange(n):
		array[i] = int(raw_input("Enter element " + str(i+1) + ": "))

	root = minTree(array)
	inOrder(root)