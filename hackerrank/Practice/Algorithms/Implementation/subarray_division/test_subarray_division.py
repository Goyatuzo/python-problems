import unittest

from subarray_division import subarray_division 

class TestSubarrayDivision(unittest.TestCase):
    def test_given(self):
        self.assertEqual(2, subarray_division([2, 2, 1, 3, 2], 4, 2))

    def test_problem(self):
        self.assertEqual(2, subarray_division([1, 2, 1, 3, 2], 3, 2))

    def test_second(self):
        self.assertEqual(0, subarray_division([1, 1, 1, 1, 1, 1], 3, 2))

    def test_three(self):
        self.assertEqual(1, subarray_division([4], 4, 1))

if __name__ == '__main__':
    unittest.main()

