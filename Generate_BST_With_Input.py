class Node:
	def __init__ (self, value, left = None, right = None):
		self._value = value
		self._left = left
		self._right = right

	def __repr__(self):
		return str(self._value)

def generateBST():

	n = int(raw_input('Enter number of elements: '))
	root = None

	if n > 0:
		root = Node(int(raw_input("Enter element " + str(1) + ": ")))
	else:
		print 'Number of elements must be greater than 0'
		exit()

	for i in xrange(n-1):
		temp = Node(int(raw_input("Enter element " + str(i+2) + ": ")))
		insertNode(root, temp)

	return root

def insertNode(root, node):
	# Assuming no duplicates being inserted
	if (node._value < root._value):
		if root._left is None:
			root._left = node
		else:
			insertNode(root._left, node)
	else:
		if root._right is None:
			root._right = node
		else:
			insertNode(root._right, node)		
