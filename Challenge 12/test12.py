import unittest

from mycode import *


class MyFirstTests():

    def test_validate(self):
        self.assertEqual(1234123412341234, "Card number OK")

    def test_pan(self):
        self.assertEqual(1234123412)

    def test_checksum(self):
        self.assertEqual(4)

    def test_issue(self):
        self.assertEqual(34, "American Express")
    
    def test_isReal(self):
        self.assertEqual()

    def test_isReal2(self):
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
