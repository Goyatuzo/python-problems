import unittest

from between_two_sets import getTotalX

class TestBetweenTwoPoints(unittest.TestCase):
    def test_self(self):
        self.assertEqual(set([6, 12, 18, 36]), getTotalX([6], [36]))

    def test_given(self):
        self.assertEqual(set([4, 8, 16]), getTotalX([2, 4], [16, 32, 96]))

    def test_problem_statement(self):
        self.assertEqual(set([6, 12]), getTotalX([2, 6], [24, 36]))
        
    def test_submission(self):
        self.assertEqual(set([12, 24]), getTotalX([3, 4], [24, 48]))

    def test_primes(self):
        self.assertEqual(set([]), getTotalX([1, 3], [5, 7, 11]))

    def test_case_1(self):
        self.assertEqual(0, len(getTotalX([100, 99, 98, 97, 96, 95, 94, 93, 92,
            91], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

    def test_case_3(self):
        self.assertEqual(2, len(getTotalX([3, 9, 6], [36, 72])))

    def test_case_4(self):
        self.assertEqual(9, len(getTotalX([1], [100])))

if __name__ == '__main__':
    unittest.main()
