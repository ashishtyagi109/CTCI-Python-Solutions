from Generate_BST_With_Input import *

def successor(node):
	if node._right is not None:
		return leftMost(node._right)
	return checkParent(node._parent, node)

def leftMost(node):
	while node._left is not None:
		node = node._left
	return node

def checkParent(parent, node):
	if parent is None:
		return None
	if node == parent._left:
		return parent
	else:
		return checkParent(parent._parent, parent)

def findInTree(root, value):
	while root is not None:
		if value < root._value:
			root = root._left
		elif value > root._value:
			root = root._right
		else:
			break # value = root._value
	return root

if __name__ == '__main__':
	root = generateBST()

	input = int(raw_input('Enter value of node whose successor is required: '))
	node = findInTree(root, input)
	if node is None:
		print 'Value not found in tree'
	else:
		successor = successor(node)
		if successor is None:
			print 'No successor for input node'
		else:
			print 'successor is: ', successor