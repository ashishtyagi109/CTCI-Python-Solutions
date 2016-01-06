class Node:
	def __init__ (self, value, left = None, right = None, parent = None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def __repr__(self):
		return str(self.value)

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
	if (node.value <= root.value):
		if root.left is None:
			root.left = node
			node.parent = root
		else:
			insertNode(root.left, node)
	else:
		if root.right is None:
			root.right = node
			node.parent = root
		else:
			insertNode(root.right, node)		
