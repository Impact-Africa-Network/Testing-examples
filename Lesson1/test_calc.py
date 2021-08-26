# the naming convention is to start with test_ and what you are testing i.e test_calc
# when running python it shows which methods represents a test case

import unittest   # You dont have to download it, found in the standard library
import calc         # import the module you want to test

# create test cases for the modules you want to test

class TestCalc(unittest.TestCase): # gives us a lot of testing capabilities 

    #test add function
    def test_add(self):  #any method in a class, takes self as an argument
        self.assertEqual(calc.add(5, 10) , 15)
        self.assertEqual(calc.add(-1, 1) , 0)
        self.assertEqual(calc.add(-1, -1) , -2)

    #test subtract function
    def test_subtract(self):  #any method in a class, takes self as an argument
        self.assertEqual(calc.subtract(10, 5) , 5)
        self.assertEqual(calc.subtract(-1, 1) , -2)
        self.assertEqual(calc.subtract(-1, -1) , 0)

    #test multiply function
    def test_multiply(self):  #any method in a class, takes self as an argument
        self.assertEqual(calc.multiply(5, 10) , 50)
        self.assertEqual(calc.multiply(-1, 1) , -1)
        self.assertEqual(calc.multiply(-1, -1) , 1)

    #test divide function
    def test_divide(self):  #any method in a class, takes self as an argument
        self.assertEqual(calc.divide(10, 5) , 2)
        self.assertEqual(calc.divide(-1, 1) , -1)
        self.assertEqual(calc.divide(-1, -1) , 1)
        self.assertEqual(calc.divide(5, 2) , 2.5)

if __name__ == '__main__':   #if we run this module directly, run the code within the conditional
    unittest.main()