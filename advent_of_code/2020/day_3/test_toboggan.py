import unittest

from toboggan import tobaggan_one

class TestToboggan(unittest.TestCase):
    def test_given_one(self):

        s = """..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#"""

        self.assertEqual(7, tobaggan_one(s))


if __name__ == '__main__':
    unittest.main()
