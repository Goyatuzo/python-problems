import unittest

from between_two_sets import getTotalX

class TestBetweenTwoPoints(unittest.TestCase):
    def test_given(self):
        self.assertEqual(set([4, 8, 16]), getTotalX([2, 4], [16, 32, 96]))

    def test_problem_statement(self):
        self.assertEqual(set([6, 12]), getTotalX([2, 6], [24, 36]))

    def test_submission(self):
        self.assertEqual(set([12, 24]), getTotalX([3, 4], [24, 48]))

if __name__ == '__main__':
    unittest.main()
