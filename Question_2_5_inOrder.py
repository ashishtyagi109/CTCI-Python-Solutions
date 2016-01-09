from LinkedList_Helpers import *
from Question_2_5_reversed import *

def sumLists(head1, head2):
	head1 = reverseList(head1)
	head2 = reverseList(head2)
	return sumListsReverse(head1, head2)

def main():
	print 'Number 1 in forward order: '
	head1 = generateList()
	print '\nNumber 2 in forward order: '
	head2 = generateList()

	sumList = sumLists(head1, head2)
	print '\nThe sum of ' + str(getList(head1)) + ' and ' + str(getList(head2)) \
	+ ' is ' + str(getList(sumList))

if __name__ == '__main__':
	main()
