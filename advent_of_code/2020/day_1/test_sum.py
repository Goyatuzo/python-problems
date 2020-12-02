import unittest

from sum import sum_aoc

class TestSumAOC(unittest.TestCase):
    def test_given(self):
        self.assertEqual(514579, sum_aoc([1721,
        979,
        366,
        299,
        675,
        1456], 2020))


if __name__ == '__main__':
    unittest.main()
