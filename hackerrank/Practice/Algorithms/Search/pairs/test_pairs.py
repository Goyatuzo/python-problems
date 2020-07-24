import unittest

from pairs import pairs 


class TestPairs(unittest.TestCase):
    def test_in_problem(self):
        self.assertEqual(3, pairs(1, [1, 2, 3, 4]))

    def test_sample(self):
        self.assertEqual(3, pairs(2, [1, 5, 3, 4, 2]))


if __name__ == '__main__':
    unittest.main()
