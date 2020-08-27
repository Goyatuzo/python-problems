import unittest

from mere_array import mere_array as foo 

class TestMereArray(unittest.TestCase):
	def test_given(self):
		self.assertEqual('YES', foo([8]))
	
	def test_given_two(self):
		self.assertEqual('YES', foo([4, 3, 6, 6, 2, 9]))

if __name__ == '__main__':
	unittest.main()
