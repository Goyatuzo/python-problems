import unittest

from mysterious_present import mysterious_present as foo

# The dictionary is stored across the three test cases
class TestMysteriousPresent(unittest.TestCase):
    def test_given(self):
        self.assertEqual((1, '1'), foo(1, 1, [(2, 2), (2, 2)]))

    def test_given_two(self):
        self.assertEqual((3, '1 3 2'), foo(3, 3, [(5, 4), (12, 11), (9, 8)]))


    def test_self(self):
        self.assertEqual((0, ''), foo(2, 2, [(1, 1)]))
    
    def test_test(self):
        self.assertEqual((0, ''), foo(13, 13, [(13, 13), (4, 4), (10, 10), (7, 7), (1, 1), (13, 13)]))


    def test_test_two(self):
        self.assertEqual((2, '4 3'), foo(1000, 998, [(5002, 5005), (5003, 5004), (5003, 5002), (5002, 5001), (5002, 5002)]))

    def test_self_two(self):
        self.assertEqual((1, '2'), foo(5, 5, [(6, 7), (6, 6)]))
        self.assertEqual((1, '2'), foo(5, 5, [(7, 6), (6, 6)]))

    def test_16(self):
        self.assertEqual(3, '2 1 3', foo(6134, 8495, [
            (9045, 8632),
            (6552, 8552),
            (9429, 8736),
            (6680, 9984)
        ]))

    

if __name__ == '__main__':
    unittest.main()
