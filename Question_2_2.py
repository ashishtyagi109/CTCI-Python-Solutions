from LinkedList_Helpers import *

def KthFromLast(head, k):
	node = head
	tracker = head
	for i in xrange(k):
		if tracker is None:
			return None # k elements don't exist in list
		tracker = tracker.next

	while tracker is not None:
		node = node.next
		tracker = tracker.next

	return node

if __name__ == '__main__':
	head = generateList()
	k = int(raw_input('Enter value of k: '))
	answer = KthFromLast(head, k)

	if answer is None:
		print 'list contains less than {} elements'.format(k)
	else:
		print answer
