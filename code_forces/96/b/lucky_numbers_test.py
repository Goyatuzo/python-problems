import unittest

from lucky_numbers import lucky_numbers as foo

class TestLuckyNumbers(unittest.TestCase):
	def test_given_1(self):
		self.assertEqual(foo('4500', '4747'))	

	def test_given_2(self):
		self.assertEqual(foo('47', '47'))	


if __name__ == '__main__':
    unittest.main()
