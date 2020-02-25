import unittest

from ice_cream_parlor import icecreamParlor


class TestIceCreamParlor(unittest.TestCase):
    def test_given(self):
        self.assertEqual([1, 4], icecreamParlor(4, [1, 4, 5, 3, 2]))
        self.assertEqual([1, 2], icecreamParlor(4, [2, 2, 4, 3]))

    def test_given_2(self):
        self.assertEqual([2, 4], icecreamParlor(9, [1, 3, 4, 6, 7, 9]))
        self.assertEqual([3, 4], icecreamParlor(8, [1, 3, 4, 4, 6, 8]))
        self.assertEqual([1, 2], icecreamParlor(3, [1, 2]))


if __name__ == '__main__':
    unittest.main()
