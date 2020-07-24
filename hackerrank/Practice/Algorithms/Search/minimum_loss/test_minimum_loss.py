import unittest

from os import getcwd, path
from pathlib import Path
from minimum_loss import minimumLoss


class TestMinimumLoss(unittest.TestCase):
    def open_file(self, fname: str):
        with open(path.join(Path(__file__).parent, fname), 'r') as f:
            f.readline()
            price = list(map(int, f.readline().rstrip().split()))
            return price

    def test_problem(self):
        self.assertEqual(3, minimumLoss([20, 15, 8, 2, 12]))

    def test_given(self):
        self.assertEqual(2, minimumLoss([5, 10, 3]))

    def test_given_two(self):
        self.assertEqual(2, minimumLoss([20, 7, 8, 2, 5]))

    def test_input05(self):
        self.assertEqual(99727, minimumLoss(self.open_file('input05.txt')))


if __name__ == '__main__':
    unittest.main()
