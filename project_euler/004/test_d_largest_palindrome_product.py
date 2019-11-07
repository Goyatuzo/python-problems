import unittest

from d_largest_palindrome_product import *

class TestLargestPalindromeProduct(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome(10101))
        self.assertTrue(is_palindrome(1001))
        self.assertFalse(is_palindrome(12))
        self.assertFalse(is_palindrome(123421))

    def test_given(self):
        self.assertEqual(101101, largest_palindrome(101110))
        self.assertEqual(793397, largest_palindrome(800000))


if __name__ == '__main__':
    unittest.main()