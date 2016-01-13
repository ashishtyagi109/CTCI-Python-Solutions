import unittest
from Question_8_3 import *

class MagicIndexTests(unittest.TestCase):

	def test_no_magic_index(self):
		arr = [i+1 for i in xrange(10)]
		self.assertEqual(magicIndex(arr), -1)

	def test_magic_index(self):
		arr = [i+1 for i in xrange(10)]
		arr[4] = 4
		self.assertEqual(magicIndex(arr), 4)



if __name__ == '__main__':
	unittest.main()