import unittest

from between_two_sets import getTotalX

class TestBetweenTwoPoints(unittest.TestCase):
    def test_given(self):
        self.assertEqual(3, getTotalX([2, 4], [16, 32, 96]))

if __name__ == '__main__':
    unittest.main()
