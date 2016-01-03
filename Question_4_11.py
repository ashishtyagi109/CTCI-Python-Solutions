# Only the getRandomNode function is defined.
# We will be assuming that the insert and delete functions have been modified \
# such that every node knows the size of its subtree

def getRandomNode(root):
	i = random.randint(0, root._size - 1)
	return getIthNode(root, i)

def getIthNode(node, i):
	leftsize = 0 if node._left is None else node._left._size
	if i < leftsize:
		return getIthNode(node._left, i)
	if i == leftsize:
		return node
	if i > leftsize:
		return getIthNode(node._right, i - (node._left._size+1))