from Generate_BST_With_Input import *

def checkBST(root):
	return checkRange(root)

def checkRange(node, max = None, min = None):
	if node is None:
		return True
	# left <= current < right
	if (min is not None and node._value <= min or max is not None and node._value > max):
		return False

	if not checkRange(node._left, node._value, min):
		return False
	if not checkRange(node._right, max, node._value):
		return False

	return True

if __name__ == '__main__':
	root = generateBST()
	print checkBST(root)