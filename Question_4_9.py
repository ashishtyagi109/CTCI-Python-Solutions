from Generate_BST_With_Input import *

def BSTseq(root):
	if root is None:
		print []
		exit()
	curArray = []
	options = [root]
	getAllArr(curArray, options)

def getAllArr(curArr, options):
	if not options: # Empty
		print curArr

	for i in xrange(len(options)):
		optionsCopy = options[:] # Required because lines 20 and 22 update options. So 24 can't 'fix' list
		node = optionsCopy.pop(i)
		curArr.append(node)
		if node.left is not None:
			optionsCopy.append(node.left)
		if node.right is not None:
			optionsCopy.append(node.right)
		getAllArr(curArr, optionsCopy)
		# options.insert(i, node) # Fix damaged list after recursive call to getAllArr
		curArr.pop() # Return curArr to original state

if __name__ == '__main__':
	root = generateBST()
	BSTseq(root)