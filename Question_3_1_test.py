import unittest
from Question_3_1 import *

class TripleStacksTests(unittest.TestCase):
	
	def test_popEmptyStack1(self):
		stack = FixedSizeMultiStack(3)
		self.assertRaises(EmptyStackError, stack.pop, 1)

	def test_popEmptyStack2(self):
		stack = FixedSizeMultiStack(3)
		stack.push(1, 'something')
		stack.pop(1)
		self.assertRaises(EmptyStackError, stack.pop, 1)

	def test_pushAndPeek(self):
		stack = FixedSizeMultiStack(3)
		stack.push(1, 'something')
		expected = 'something'
		actual = stack.peek(1)
		self.assertEqual(expected, actual)

	def test_peekEmptyStack(self):
		stack = FixedSizeMultiStack(3)
		self.assertRaises(EmptyStackError, stack.peek, 1)	
		
	def test_pushOverCapacity(self):
		stack = FixedSizeMultiStack(3)
		stack.push(1, 'something')
		stack.push(1, 'more')
		stack.push(1, 'and more')
		self.assertRaises(StackFullError, stack.push, 1, 'no more')

if __name__ == '__main__':
	unittest.main()