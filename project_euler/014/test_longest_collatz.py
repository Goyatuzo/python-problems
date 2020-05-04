import unittest

from longest_collatz import longest_collatz

class TestLongestCollatz(unittest.TestCase):
    def test_10(self):
        self.assertEqual(9, longest_collatz(10))

    def test_15(self):
        self.assertEqual(9, longest_collatz(15))

    def test_20(self):
        self.assertEqual(19, longest_collatz(20))

if __name__ == '__main__':
    unittest.main()
