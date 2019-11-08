import unittest

from three_and_five import solve_unoptimized

class TestThreeAndFive(unittest.TestCase):
    def test_given(self):
        self.assertEqual(23, solve_unoptimized(10))

    def test_less_than_ten(self):
        self.assertEqual(0, solve_unoptimized(1))
        self.assertEqual(0, solve_unoptimized(2))
        self.assertEqual(0, solve_unoptimized(3))
        self.assertEqual(3, solve_unoptimized(4))
        self.assertEqual(3, solve_unoptimized(5))
        self.assertEqual(8, solve_unoptimized(6))
        self.assertEqual(14, solve_unoptimized(7))
        self.assertEqual(14, solve_unoptimized(8))
        self.assertEqual(14, solve_unoptimized(9))

if __name__ == '__main__':
    unittest.main()