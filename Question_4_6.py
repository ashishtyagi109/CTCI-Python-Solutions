from Generate_BST_With_Input import *

def successor(node):
	if node.right is not None:
		return leftMost(node.right)
	return checkParent(node.parent, node)

def leftMost(node):
	while node.left is not None:
		node = node.left
	return node

def checkParent(parent, node):
	if parent is None:
		return None
	if node == parent.left:
		return parent
	else:
		return checkParent(parent.parent, parent)

def findInTree(root, value):
	while root is not None:
		if value < root.value:
			root = root.left
		elif value > root.value:
			root = root.right
		else:
			break # value = root.value
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