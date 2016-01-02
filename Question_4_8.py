def commonAncestorHelper(root, p, q):
	if root is None:
		return root, False
	if root == p and root == q:
		return root, True

	x, ancOnLeft = commonAncestorHelper(root._left, p, q)
	if ancOnLeft: # ancestor already found on left
		return x, True

	y, ancOnRight = commonAncestorHelper(root._right, p, q)
	if ancOnRight: # ancestor already found on right
		return y, True

	if x is not None and y is not None:
		return root, True
	elif root == p or root == q:
		# If root is p or q AND we found either p or q in one of the subtrees, \ 
		# then root is an ancestor
		isAncestor = x is not None or y is not None
		return root, isAncestor
	else:
		return y if x is None else x, False # Returns non-None value, or None if both x and y are None

def firstCommonAncestor(root, p, q):
	node, ancFound = commonAncestorHelper(root, p, q)
	if ancFound:
		return node
		
	return None