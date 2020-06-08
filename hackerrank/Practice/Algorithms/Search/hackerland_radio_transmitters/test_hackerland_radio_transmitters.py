import unittest

from hackerland_radio_transmitters import hackerlandRadioTransmitters

class TestHackerlandRadioTransmitters(unittest.TestCase):
    def test_all_spread(self):
        self.assertEqual(5, len(hackerlandRadioTransmitters([1, 3, 5, 7, 9],
            1)))
        self.assertEqual(3, len(hackerlandRadioTransmitters([2, 3, 5, 7, 8, 9],
            1)))
        self.assertEqual(2, len(hackerlandRadioTransmitters([1, 4, 5, 6], 1)))

    def test_problem(self):
        self.assertEqual(3, len(hackerlandRadioTransmitters([1, 2, 3, 5, 9],
            1)))
    
    def test_given(self):
        self.assertEqual(2, len(hackerlandRadioTransmitters([1, 2, 3, 4, 5],
            1)))

    def test_run(self):
        self.assertEqual(3, len(hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9,
            12, 11], 2)))

if __name__ == '__main__':
    unittest.main()
