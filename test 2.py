import unittest

from richter import *


class MyFirstTests(unittest.TestCase):

    def test_in_joules(self):
        joules = in_joules(2)
        self.assertEqual(joules, 63095734.448019296)

    def test_in_TNT(self):
        TNT = in_TNT(2)
        self.assertEqual(TNT, 4.780114722753346e-10)

if __name__ == '__main__':
    unittest.main()
