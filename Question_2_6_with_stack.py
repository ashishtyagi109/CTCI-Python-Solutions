from LinkedList_Helpers import *

def checkPalindrome(head):
	firstHalf = []
	fast = head
	slow = head
	odd = False
	while fast is not None:
		firstHalf.append(slow.value)
		slow = slow.next
		fast = fast.next
		if fast is not None:
			fast = fast.next
		else:
			odd = True

	if odd:
		firstHalf.pop()

	while slow is not None:
		if slow.value != firstHalf.pop():
			return False
		slow = slow.next
	return True

if __name__ == '__main__':
	head = generateList()
	if checkPalindrome(head):
		print 'List is a palindrome'
	else:
		print 'List is not a palindrome'