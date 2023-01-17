import unittest

from football import football as foo

class TestFootball(unittest.TestCase):
	def test_given_1(self):
		self.assertFalse(foo('001001'))

	def test_given_2(self):
		self.assertTrue(foo('1000000001'))


if __name__ == '__main__':
    unittest.main()
