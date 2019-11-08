import unittest

from three_and_five import solve_unoptimized

class TestThreeAndFive(unittest.TestCase):
    def test_given(self):
        self.assertEqual(23, solve_unoptimized(10))

    def test_manual(self):
        self.assertEqual(14, solve_unoptimized(9))

if __name__ == '__main__':
    unittest.main()