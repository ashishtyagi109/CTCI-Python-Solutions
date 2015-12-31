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