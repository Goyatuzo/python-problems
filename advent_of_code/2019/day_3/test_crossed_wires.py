import unittest

from crossed_wires import solve_first


class TestCrossedWires(unittest.TestCase):
    def test_part_one_given(self):
        self.assertEqual(6, solve_first("R8,U5,L5,D3", "U7,R6,D4,L4"))
        self.assertEqual(159, solve_first(
            "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"))
        self.assertEqual(135, solve_first(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))

    def test_part_two_given(self):
        self.assertEqual(30, solve_first("R8,U5,L5,D3", "U7,R6,D4,L4"))
        self.assertEqual(610, solve_first(
            "R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"))
        self.assertEqual(410, solve_first(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))


if __name__ == '__main__':
    unittest.main()
