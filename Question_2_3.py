from LinkedList_Helpers import *

def deleteNode(node):
	if node is None or node.next is None:
		return False # Failure
	node.value = node.next.value
	node.next = node.next.next
	return True

if __name__ == '__main__':
	head = generateList()
	valToDelete = int(raw_input('Enter value to delete: '))
	nodeToDelete = findNodeInList(head, valToDelete)

	print 'Initial List: '
	print getList(head)

	deleteNode(nodeToDelete)
	print 'New List: '
	print getList(head)