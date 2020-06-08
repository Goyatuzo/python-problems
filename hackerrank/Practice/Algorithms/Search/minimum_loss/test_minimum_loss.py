import unittest

from minimum_loss import minimumLoss


class TestMinimumLoss(unittest.TestCase):
    def test_problem(self):
        self.assertEqual(3, minimumLoss([20, 15, 8, 2, 12]))

    def test_given(self):
        self.assertEqual(2, minimumLoss([5, 10, 3]))


if __name__ == '__main__':
    unittest.main()
