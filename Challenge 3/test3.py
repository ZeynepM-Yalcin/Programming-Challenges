import unittest

from trick_99 import *


class MyFirstTests(unittest.TestCase):

    def check_input_False(self):
        self.assertEqual(check_input(5,1,49), False)
    
    def check_input_False(self):
        self.assertEqual(check_input(0,1,49), True)



    def calculations(self):
        
        self.assertEqual(calculations(33, 77), 44)

if __name__ == '__main__':
    unittest.main()
