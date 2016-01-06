def generateList():
	
	n = int(raw_input('Enter number of elements: '))
	head = None

	if n > 0:
		head = Node(int(raw_input("Enter element " + str(1) + ": ")))
	else:
		print 'Number of elements must be greater than 0'
		exit()

	tail = head
	for i in xrange(n-1):
		temp = Node(int(raw_input("Enter element " + str(i+2) + ": ")))
		insertAtEnd(tail, temp)
		tail = tail.next

	return head

class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

	def __repr__(self):
		return str(self.value)

def insertAtEnd(tail, node):
	tail.next = node
	node.prev = tail

def printList(head):
	while head is not None:
		print head
		head = head.next

def getList(head):
	linkedList = []
	while head is not None:
		linkedList.append(head.value)
		head = head.next
	return linkedList