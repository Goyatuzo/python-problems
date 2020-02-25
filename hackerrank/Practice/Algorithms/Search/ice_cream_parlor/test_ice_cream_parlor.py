import unittest

from ice_cream_parlor import icecreamParlor


class TestIceCreamParlor(unittest.TestCase):
    def test_in_problem(self):
        self.assertEqual([1, 4], icecreamParlor(6, [1, 3, 4, 5, 6]))

    def test_given(self):
        self.assertEqual([1, 4], icecreamParlor(4, [1, 4, 5, 3, 2]))
        self.assertEqual([1, 2], icecreamParlor(4, [2, 2, 4, 3]))

    def test_given_2(self):
        self.assertEqual([2, 4], icecreamParlor(9, [1, 3, 4, 6, 7, 9]))
        self.assertEqual([3, 4], icecreamParlor(8, [1, 3, 4, 4, 6, 8]))
        self.assertEqual([1, 2], icecreamParlor(3, [1, 2]))

    def test_given_3(self):
        self.assertEqual([2, 3], icecreamParlor(100, [5, 75, 25]))
        self.assertEqual([29, 46], icecreamParlor(542, [230, 863, 916, 585, 981, 404, 316, 785, 88, 12, 70, 435, 384, 778, 887, 755, 740, 337, 86, 92, 325, 422, 815, 650, 920, 125, 277, 336, 221, 847, 168, 23, 677, 61, 400, 136, 874, 363, 394, 199, 863, 997, 794, 587, 124, 321, 212, 957, 764, 173, 314, 422, 927, 783, 930, 282, 306, 506, 44, 926, 691, 568, 68, 730, 933, 737, 531, 180, 414, 751, 28, 546, 60, 371, 493, 370, 527, 387, 43, 541, 13, 457, 328, 227, 652, 365, 430, 803, 59, 858, 538, 427, 583, 368, 375, 173, 809, 896, 370, 789]))

if __name__ == '__main__':
    unittest.main()
