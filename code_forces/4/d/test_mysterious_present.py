import unittest

from mysterious_present import mysterious_present as foo

# The dictionary is stored across the three test cases
class TestMysteriousPresent(unittest.TestCase):
    def test_given(self):
        self.assertEqual((1, '1'), foo(1, 1, [(2, 2), (2, 2)]))

    def test_given_two(self):
        self.assertEqual((3, '1 3 2'), foo(3, 3, [(5, 4), (12, 11), (9, 8)]))
    

if __name__ == '__main__':
    unittest.main()
