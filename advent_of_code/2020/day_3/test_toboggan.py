import unittest

from toboggan import tobaggan_one, tobaggan_gen, tobaggan_two

class TestToboggan(unittest.TestCase):
    s =  """..##.......
            #...#...#..
            .#....#..#.
            ..#.#...#.#
            .#...##..#.
            ..#.##.....
            .#.#.#....#
            .#........#
            #.##...#...
            #...##....#
            .#..#...#.#""".replace(' ', '').split('\n')

    def test_given_one(self):
        self.assertEqual(7, tobaggan_one(self.s))

    def test_given_two_one(self):
        self.assertEqual(2, tobaggan_gen(self.s, 1, 1))

    def test_given_two_two(self):
        self.assertEqual(7, tobaggan_gen(self.s, 3, 1))

    def test_given_two_three(self):
        self.assertEqual(3, tobaggan_gen(self.s, 5, 1))

    def test_given_two_four(self):
        self.assertEqual(4, tobaggan_gen(self.s, 7, 1))

    def test_given_two_five(self):
        self.assertEqual(2, tobaggan_gen(self.s, 1, 2))

    def test_given_two(self):
        self.assertEqual(336, tobaggan_two(self.s))

if __name__ == '__main__':
    unittest.main()
