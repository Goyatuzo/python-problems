import unittest

from toboggan import toboggan_one

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

        self.assertEqual(7, toboggan_one(s))


if __name__ == '__main__':
    unittest.main()
