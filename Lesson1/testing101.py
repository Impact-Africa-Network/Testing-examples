
# Plan

# Begin with simple tests
# Examples of testing in python 
# Real world testing of modules in django
# Examples of testing in React


# INTRODUCTION TO UNIT TESTING USING PYTHON

# Especially useful when working with large project 
# Good tests ensures that any updates and refactorings dont have any unintended consequences or break code
# If you update a function it could break other parts of the project even when the actual function is working properly
# Unit tests Ensure everything is working properly and if not show you exactly whats broken 
# What people normally do is write print statements - this is hard to maintain and automate
# for testing multiple functions there is no way to see what failed or succeded


# RESOURCES
# unit test python documentation -> https://docs.python.org/3/library/unittest.html
# Tuts -> https://www.youtube.com/watch?v=6tNS--WetLI

# GETTING STARTED
# we will use the unittest module and inherit the class TestCase class
# we use the assert functions 

# RUNNING THE TEST
# NB:  running python test_calc.py wont work right away
# python -m unittest test_calc.py

# THINGS TO CONSIDER 
# Test the edge cases i.e negative numbers 
# Make sure your tests are named properly i.e convention is test_name - start with the test_
# If you catch problems that might not have been caught by the test always make sure to always update your tests

