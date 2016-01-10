from LinkedList_Helpers import Node

def loopDetect(head):
	slow = head
	fast = head

	while (fast is not None and fast.next is not None):
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			break

	if (fast is None or fast.next is None):
		return None # No loop exists

	fast = head
	# Second collision
	while (slow != fast):
		slow = slow.next
		fast = fast.next

	return slow # or fast
