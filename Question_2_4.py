from LinkedList_Helpers import *

def partition(head, value):
	listHead = head
	listTail = head
	node = head # Just to remove ambiguity

	while node is not None:
		next = node.next
		if node.value < value:
			node.next = listHead
			listHead = node
		else:
			listTail.next = node
			listTail = node
		node = next

	listTail.next = None
	return listHead

if __name__ == '__main__':
	head = generateList()
	value = int(raw_input('Enter value to partition about: '))

	print 'Initial List: '
	print getList(head)

	answer = partition(head, value)
	print 'List after partition: '
	print getList(answer)