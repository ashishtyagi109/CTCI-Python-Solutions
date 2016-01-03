from Generate_BST_With_Input import *
from cStringIO import StringIO

def checkSubTree(t1, t2):
	preOrderStrT1 = StringIO()
	preOrderStrT2 = StringIO()

	preOrder(t1, preOrderStrT1)
	preOrder(t2, preOrderStrT2)
	strT1 = preOrderStrT1.getvalue()
	strT2 = preOrderStrT2.getvalue()

	return strT2 in strT1

def preOrder(root, strRep):
	if root is None:
		strRep.write('X')
		return
	strRep.write(str(root._value))
	preOrder(root._left, strRep)
	preOrder(root._right, strRep)

if __name__ == '__main__':

	print 'Tree 1: '
	root1 = generateBST()
	print '\nTree 2: '
	root2 = generateBST()
	if checkSubTree(root1, root2):
		print 'T2 is a subtree of T1!'
	else:
		print 'T2 is not a subtree of T1'


