import unittest

from apple_and_orange import countApplesAndOranges

class TestAppleAndOrange(unittest.TestCase):
    def test_problem(self):
        self.assertEqual((1, 2), countApplesAndOranges(7, 10, 4, 12, [2, 3,
            -4], [3, -2, -4]))

    def test_given(self):
        self.assertEqual((1, 1), countApplesAndOranges(7, 11, 5, 15, [-2, 2,
            1], [5, -6]))


if __name__ == '__main__':
    unittest.main()

