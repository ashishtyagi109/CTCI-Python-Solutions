from LinkedList_Helpers import *

# With extra space allowed
# We will assume we have a doubly linked list
def removeDuplicates(head):
	if head is None:
		return head
	duplicates = {}

	node = head
	while node is not None:
		if node.value in duplicates:
			# this will not be entered when node = head
			node.prev.next = node.next
			if node.next is not None:
				node.next.prev = node.prev
		else:
			duplicates[node.value] = None
		node = node.next

	return head

if __name__ == '__main__':
	head = generateList()
	print 'Initial list: '
	print getList(head)

	removeDuplicates(head)
	print '\nList without duplicates: '
	print getList(head)