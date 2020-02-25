import unittest

from ice_cream_parlor import icecreamParlor


class TestIceCreamParlor(unittest.TestCase):
    def test_given(self):
        self.assertEqual([1, 4], icecreamParlor(4, [1, 4, 5, 3, 2]))
        self.assertEqual([1, 2], icecreamParlor(4, [2, 2, 4, 3]))


if __name__ == '__main__':
    unittest.main()
