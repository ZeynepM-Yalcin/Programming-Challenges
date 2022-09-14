import unittest

from Rod_conversions import *


class MyFirstTests(unittest.TestCase):

    def test_rod_to_meters(self):
        meters = rod_to_meters(10)
        self.assertEqual(meters,50.292)

    def test_meters_to_feet(self):
        feet = meters_to_feet(10)
        self.assertEqual(feet,32.808398950131235)
        
    def test_meters_to_miles(self):
        meters = meters_to_miles(10)
        self.assertEqual(miles,0.03125007767159208)
        
    def test_rods_to_furlongs(self):
        meters = rods_to_furlongs(10)
        self.assertEqual(furlongs,0.25)
        
    def test_miles_in_minutes(self):
        meters = miles_in_minutes(10)
        self.assertEqual(minutes,0.000520834627859868)
        
if __name__ == '__main__':
    unittest.main()
