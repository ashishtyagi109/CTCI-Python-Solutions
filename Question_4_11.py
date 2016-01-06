# Only the getRandomNode function is defined.
# We will be assuming that the insert and delete functions have been modified \
# such that every node knows the size of its subtree

def getRandomNode(root):
	i = random.randint(0, root.size - 1)
	return getIthNode(root, i)

def getIthNode(node, i):
	leftsize = 0 if node.left is None else node.left.size
	if i < leftsize:
		return getIthNode(node.left, i)
	if i == leftsize:
		return node
	if i > leftsize:
		return getIthNode(node.right, i - (node.left.size+1))