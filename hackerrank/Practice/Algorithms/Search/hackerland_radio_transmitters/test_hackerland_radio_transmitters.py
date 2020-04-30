import unittest

from hackerland_radio_transmitters import hackerlandRadioTransmitters

class TestHackerlandRadioTransmitters(unittest.TestCase):
    def test_given(self):
        self.assertEqual(2, hackerlandRadioTransmitters([1, 2, 3, 4, 5], 1))

if __name__ == '__main__':
    unittest.main()
