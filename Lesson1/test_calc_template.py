# first import the requred modules for testing
import unittest

# Import the file/module you want to testing
import calc_template


# create test cases for the modules you want to test


## create a test class and inherit the TestCase class from unittest
## from the TestCase you'll find multiple assertions
### Define your different testing functions within the class
    ### def test_add(self):
    ###     self.assertEqual(func, result)

class TestFunctions(unittest.TestCase):

    def test_add(self):  #any method in a class, takes self as an argument

        self.assertEqual(calc_template.add(2,3), 5)
        self.assertEqual(calc_template.add(-1, -5), -6)
        # self.assertEqual(calc.add(5, 10) , 15)

if __name__ == '__main__':   #if we run this module directly, run the code within the conditional
    unittest.main()
       





### create test for each function (Add, subtract, multiply, divide)



### run the test cases on the terminal using the following commmand
### ->  python -m unittest test_filename.py


### automate running the tests using the following code snippet
    ### if __name__ == '__main__':  
    ###      unittest.main()




