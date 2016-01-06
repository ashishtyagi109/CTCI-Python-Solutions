from LinkedList_Helpers import *

# With extra space not allowed
# We will assume we have a doubly linked list
def removeDuplicates(head):
	if head is None:
		return head

	node = head
	while node is not None:
		duplicateChecker = node.next
		while duplicateChecker is not None:
			if node.value == duplicateChecker.value:
				remove(duplicateChecker)
			duplicateChecker = duplicateChecker.next
		node = node.next

	return head

def remove(node):
	node.prev.next = node.next
	if node.next is not None:
		node.next.prev = node.prev

if __name__ == '__main__':
	head = generateList()
	print 'Initial list: '
	print getList(head)

	removeDuplicates(head)
	print '\nList without duplicates: '
	print getList(head)