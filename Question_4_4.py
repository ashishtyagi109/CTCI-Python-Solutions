import sys
from Generate_BST_With_Input import *
from Question_4_3 import *

def checkBalanced(root):
	# Error code is defined as (-sys.maxint - 1)
	return checkHeight(root) != (-sys.maxint - 1)

def checkHeight(node):
	if node is None:
		return -1

	leftHeight = checkHeight(node._left)
	if leftHeight == (-sys.maxint - 1):
		return (-sys.maxint - 1)

	rightHeight = checkHeight(node._right)
	if rightHeight == (-sys.maxint - 1):
		return (-sys.maxint - 1)

	if abs(leftHeight - rightHeight) > 1:
		return (-sys.maxint - 1)

	return max(leftHeight, rightHeight) +1

if __name__ == '__main__':
	root = generateBST()
	print listOfDepths(root)
	print checkBalanced(root)