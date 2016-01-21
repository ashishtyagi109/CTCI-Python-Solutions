import unittest
from Question_8_13 import *

class MaxHeightTests(unittest.TestCase):
	
	def test_one(self):
		boxes = []
		boxes.append(Box(1, 1, 10))
		boxes.append(Box(8, 8, 4))
		boxes.append(Box(9, 9, 5))
		self.assertEqual(10, maxHeight(boxes))
	

	def test_two(self):
		boxes = []
		boxes.append(Box(1, 1, 10))
		boxes.append(Box(8, 8, 5))
		boxes.append(Box(9, 9, 6))
		self.assertEqual(11, maxHeight(boxes))

if __name__ == '__main__':
	unittest.main()
