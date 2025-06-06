import pytest
#
# from pytest import
from calc import square

def test_square():
    #assert square(-3) == -3
    assert square(-2) == 4
    #assert square(-1) == -1
    assert square(-0) == -0
    assert square(0) == 0
    assert square(1) == 1
    assert square(2) == 4
    # assert square(3) == 3
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25


# you have to run program in command line using this cmd::===> pytest pyTestInPython or your other code as per naming convention:::==> pytest test_calculator

# it is better to make carious unit test otherwise it will stop on the first error triggered, so instead do this so if some of the part fails it will atleast give you 75% passed but 25% failed

def test_positive():
    assert square(1) == 1
    assert square(2) == 4
    assert square(4) == 16
    assert square(5) == 25
    assert square(9) == 81



def test_negative():
    assert square(-1) == 1
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(-9) == 81

def test_zero():
    assert square(0) == 0
    assert square(-0) == 0

def test_string():
    assert square("cat") == "cat"

def test_str():
    with pytest.raises(TypeError):
        assert square("string")


        # harvard python full course --->> 06:50:50