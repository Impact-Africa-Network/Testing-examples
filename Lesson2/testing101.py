## Awesome resources

# Django testing (https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#intro-to-testing-in-django)
# Pytest api (https://www.youtube.com/watch?v=byaxg00Gf9I)
# More on Pytest (https://www.youtube.com/watch?v=RcN26hznmk4), (https://www.youtube.com/watch?v=UMgxJvozR5A)
# Test Automation in python using selenium (https://www.youtube.com/watch?v=73qAGhXu5mM)

## Why I would test?

# --- 1. Prove that the code works as it should
# --- 2. Give examples to others of how code is used

## Types of Tests

# ---- 1: Unit Tests : isolated tests that test one specific function.
# ---- 2: Integration Tests : larger tests that focus on user behavior and testing entire applications. 
# NB: Focus on unit tests. 
# --- Write A LOT of these. 
# --- These tests are much easier to write and debug vs. integration tests, 
# --- The more you have, the less integration tests you will need.


## PYTEST MODULE (pytest.org)

# --- Most popular module for testing
# Assert is how you do testing in pytest


## difference btwn pytest and unitest

# ---(Pytest)--
# clean api
# > assert command

# ---(unitest)--
# api is more explicit
# > assertEqual
# > assertNotEqual
# > assertTrue
# > assertFalse
# > assertIs 
# > assertIsNot
# .. + 6 more


## Pytest api

# You can test multiple tests by grouping them using markers 
# You need to specify each marker before each test
# For cases you want to test all your functions individually
# import pytest 
# use decorators on each function @pytest.mark.one or @pytest.mark.two
# to run each test per marker, run the following command
# > py.test -m one

# You can group your tests in classes
# class TestClass:
# --- def test_one(self):
# ------ x = "hello world"
# ------ assert hasattr(x, "hello")


# pytest fixtures 
# -- when you want to run a code before your tests 
# > import pytest 
# > @pytest.mark.fixtures

# pytest parametrize
# -- this is when you want to test multiple parameters at the same time
# > @pytest.mark.parametrize()

# pytest skip
# -- For when you want to skip a test 
# > @pytest.mark.skip()

# pytest xfail
# -- for failing test. the test should fail
# > @pytest.mark.xfail()


## Testing for errors

# You can test for errors that occur in your website such as 
# How python handles errors is by raising exceptions
# You can pass what info you want to show for the error to provide good diagnostic error messages

## Getting started

# pip install pipenv
# pipenv shell
# pip install pytest
# > pytest (this command will look for files that match test_name.py)















## ------ other notes on python-----##

# There is a difference btwn a function and a method 
# A function doesnt not exist in a class
# A class is a way to group behaviour together
# A function is not intended to keep track of any behaviour - Pass inputs and get some output
# For a method, you have to pass self or however you want to name it as the first attribute to the method ie. def(self, a, b)