from LinkedList_Helpers import *

def checkPalindrome(head):
	reverse = reverseList(head)
	return isEqual(head, reverse)

if __name__ == '__main__':
	head = generateList()
	if checkPalindrome(head):
		print 'List is a palindrome'
	else:
		print 'List is not a palindrome'