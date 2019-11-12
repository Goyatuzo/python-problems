import unittest

from cyclical_figurate_numbers import solve_first


class TestCyclicalFigurateNumbers(unittest.TestCase):
    def test_given(self):
        
        self.assertAlmostEqual([8128, 2882, 8281], solve_first(3))


if __name__ == '__main__':
    unittest.main()