from LinkedList_Helpers import *

def intersection(head1, head2):
	size1, tail1 = getSizeAndTail(head1)
	size2, tail2 = getSizeAndTail(head2)

	if tail1 != tail2:
		return None # No Intersection exists

	longer = head1 if size1 > size2 else head2
	smaller = head2 if size1 > size2 else head1

	longer = getKthNode(longer, abs(size1 - size2))

	while (smaller != longer):
		smaller = smaller.next
		longer = longer.next
	return longer

def getSizeAndTail(head):
	if head is None:
		return 0, None

	size = 1
	while head.next is not None:
		size += 1
		head = head.next

	return size, head

if __name__ == '__main__':
	head1 = generateList()
	head2 = Node(7, head1)

	intersect = intersection(head1, head2)
	if intersect is None:
		print 'No intersection exists'
	else:
		print 'Value of intersecting node is: ', intersect


		