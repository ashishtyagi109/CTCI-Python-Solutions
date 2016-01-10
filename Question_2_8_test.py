import unittest
from Question_2_8 import *

class LoopDetectTests(unittest.TestCase):

	def test_loopAt2(self):
		head = Node(1)
		temp = Node(2)
		head.next = temp
		tail = temp

		for i in xrange(3, 10):
			tail.next = Node(i)
			tail = tail.next

		tail.next = temp # Loop starts at 2
		self.assertIs(loopDetect(head), temp)

	def test_noLoop(self):
		head = Node(1)
		tail = head

		for i in xrange(2, 10):
			tail.next = Node(i)
			tail = tail.next

		self.assertIsNone(loopDetect(head))

if __name__ == '__main__':
	unittest.main()
