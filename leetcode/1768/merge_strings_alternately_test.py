import unittest

from merge_strings_alternately import merge_strings_alternately as foo

class Test_Merge_Strings_Alternately(unittest.TestCase):
	def test_given_1(self):
        self.assertEqual(foo("abc", "pqr"), "apbqcr")

	def test_given_2(self):
        self.assertEqual(foo("ab", "pqrs"), "apbqrs")

	def test_given_3(self):
        self.assertEqual(foo("abcd", "pq"), "apbqcd")


if __name__ == '__main__':
    unittest.main()
