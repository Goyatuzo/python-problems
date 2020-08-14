import unittest

from watermelon import watermelon 

class TestWatermelon(unittest.TestCase):
    def test_basic(self):
        self.assertEqual('YES', watermelon(8))
        self.assertEqual('NO', watermelon(7))
        self.assertEqual('NO', watermelon(5))

    def test_tests(self):
        self.assertEqual('NO', watermelon(2))
        self.assertEqual('YES', watermelon(6))
        self.assertEqual('YES', watermelon(4))

if __name__ == '__main__':
    unittest.main()
