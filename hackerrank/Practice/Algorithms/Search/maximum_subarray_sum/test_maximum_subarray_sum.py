import unittest

from maximum_subarray_sum import maximumSum 


class TestMaximumSubarraySum(unittest.TestCase):
    def test_in_problem(self):
        self.assertEqual(1, maximumSum([1, 2, 3], 2))

    def test_sample(self):
        self.assertEqual(6, maximumSum([3, 3, 9, 9, 5], 7))


if __name__ == '__main__':
    unittest.main()
