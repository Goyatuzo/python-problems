import unittest

from sum import sum_aoc_sort, sum_three

class TestSumAOC(unittest.TestCase):
    def test_given(self):
        self.assertEqual(514579, sum_aoc_sort([1721,
        979,
        366,
        299,
        675,
        1456], 2020))

    def test_given_two(self):
        self.assertEqual(241861950, sum_three([1721,
        979,
        366,
        299,
        675,
        1456], 2020))


if __name__ == '__main__':
    unittest.main()
