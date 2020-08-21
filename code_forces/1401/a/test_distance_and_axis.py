import unittest

from distance_and_axis import distance_and_axis as foo 

class TestDistanceAndAxis(unittest.TestCase):
	def test_given(self):
		self.assertEqual(0, foo(4, 0))
	
	def test_given_two(self):
		self.assertEqual(3, foo(5, 8))

	def test_given_three(self):
		self.assertEqual(1000000, foo(0, 1000000))
	
	def test_given_four(self):
		self.assertEqual(0, foo(0, 0))

	def test_given_five(self):
		self.assertEqual(1, foo(1, 0))

	def test_given_six(self):
		self.assertEqual(0, foo(1000000, 1000000))

if __name__ == '__main__':
	unittest.main()
