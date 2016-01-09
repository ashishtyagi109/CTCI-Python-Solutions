from LinkedList_Helpers import *

def sumListsReverse(head1, head2):
	"""Takes 2 lists in reverse order, returns sum in forward order"""
	
	sumHead = None
	carry = 0

	while head1 is not None and head2 is not None:
		sum = head1.value + head2.value + carry
		carry = sum/10
		sumHead = Node(sum%10, sumHead)
		head1 = head1.next
		head2 = head2.next

	remaining = head1 if head1 is not None else head2
	sumHead, carry = sumRest(sumHead, remaining, carry)

	if carry > 0:
		sumHead = Node(carry, sumHead)
	return sumHead

def sumRest(sumHead, head, carry):
	if head is None:
		return sumHead, carry

	while head is not None:
		sum = head.value + carry
		sumHead = Node(sum%10, sumHead)
		carry = sum/10
		head = head.next
	return sumHead, carry

def main():
	print 'Number 1 in reverse order: '
	head1 = generateList()
	print '\nNumber 2 in reverse order: '
	head2 = generateList()

	sumList = sumListsReverse(head1, head2)
	sumList = reverseList(sumList) # to get answer in reverse form
	print '\nThe sum of ' + str(getList(head1)) + ' and ' + str(getList(head2)) \
	+ ' is ' + str(getList(sumList))

if __name__ == '__main__':
	main()
