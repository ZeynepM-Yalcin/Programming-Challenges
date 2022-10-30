import unittest

from calculator import *


class MyFirstTests(unittest.TestCase):

    def test_op_minus(self):
        self.assertEqual(op_minus(3,4),(-1.0))

    def test_op_plus(self):
        self.assertEqual(op_plus(3,4),(7.0))
        
    def test_op_multiply(self):
        self.assertEqual(op_multiply(3,4),(12.0))
        
    def test_op_divide(self):
        self.assertEqual(op_divide(3,4),(0.75))
        
    def test_op_power(self):
        self.assertEqual(op_power(3,4),(81.0))

    def test_op_mod(self):
        self.assertEqual(op_mod(3,4),(3))

    def test_op_div(self):
        self.assertEqual(op_div(3,4),(3))

if __name__ == '__main__':
    unittest.main()
