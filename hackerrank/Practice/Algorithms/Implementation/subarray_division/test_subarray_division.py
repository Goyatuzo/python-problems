import unittest

from subarray_division import subarray_division 

class TestSubarrayDivision(unittest.TestCase):
    def test_problem(self):
        self.assertEqual(2, subarray_division([1, 2, 1, 3, 2], 3, 2))

if __name__ == '__main__':
    unittest.main()

