import pytest
from calc import Calculator

@pytest.mark.christine
def test_add():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5

@pytest.mark.skip()
def test_subtract():
    calc = Calculator()
    result = calc.subtract(10, 4)
    assert result == 5


def test_multiply():
    calc = Calculator()
    res = calc.multiply(2,2)
    assert res == 4


# > pytest
# > py.test -m christine
