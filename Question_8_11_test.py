import unittest
from Question_8_11 import *

class CoinWaysTest(unittest.TestCase):
	def test_fourCents(self):
		self.assertEqual(1, coinWays(4))
	def test_sevenCents(self):
		self.assertEqual(2, coinWays(7))
	def test_tenCents(self):
		self.assertEqual(4, coinWays(10))
	def test_fifteenCents(self):
		self.assertEqual(6, coinWays(15))

if __name__ == '__main__':
	unittest.main()
	