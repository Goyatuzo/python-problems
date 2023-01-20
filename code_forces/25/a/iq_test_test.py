import unittest

from iq_test import iq_test as foo

class Testiq_test(unittest.TestCase):
	def test_given_1(self):
		self.assertEqual(foo([2, 4, 7, 8, 10]), 3)

	def test_given_2(self):
		self.assertEqual(foo([1, 2, 1, 1]), 2)


if __name__ == '__main__':
    unittest.main()
