import unittest

from ternary_sequence import ternary_sequence as foo 

class TestTernarySequence(unittest.TestCase):
	def test_given(self):
		self.assertEqual(4, foo(2, 3, 2, 3, 3, 1))

if __name__ == '__main__':
	unittest.main()
