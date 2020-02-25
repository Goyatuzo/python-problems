import unittest

from gridland_metro import gridlandMetro


class TestGridlandMetro(unittest.TestCase):
    def test_problem(self):
        self.assertEqual(5, gridlandMetro(4, 4, 4, [[1, 1, 4], [2, 2, 4], [3, 1, 2], [4, 2, 3]]))

    def test_given(self):
        self.assertEqual(9, gridlandMetro(4, 4, 3, [[2, 2, 3], [3, 1, 4], [4, 4, 4]]))

if __name__ == '__main__':
    unittest.main()
