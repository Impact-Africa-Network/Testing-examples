
#import the Calculator class
from calc import Calculator

def test_add():
    calc =  Calculator()
    result = calc.add(2, 3)
    assert result == 5

#
def test_error():
    calc =  Calculator()
    result = calc.add(99, 1)
    assert result == 100

