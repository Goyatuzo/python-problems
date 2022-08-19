import unittest

from day_of_the_programmer import day_of_the_programmer

class TestDayOfTheProgrammer(unittest.TestCase):
    def test_0(self):
        self.assertEqual("13.09.2017", day_of_the_programmer(2017))

    def test_1(self):
        self.assertEqual("12.09.2016", day_of_the_programmer(2016))

    def test_2(self):
        self.assertEqual("12.09.1800", day_of_the_programmer(1800))


if __name__ == '__main__':
    unittest.main()

