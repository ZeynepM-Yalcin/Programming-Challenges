import unittest

from slayer import *

class TestCalc(unittest.TestCase):

    def test_calculate(self):
        self.assertEqual(calculate(142857),(428571,428571))


if __name__ == "__main__":
    unittest.main()

