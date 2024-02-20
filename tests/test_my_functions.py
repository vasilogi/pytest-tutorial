import pytest
import src.my_functions as my_functions
import time

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5
    return None

def test_divide():
    assert my_functions.divide(10, 5) == 2
    return None

def test_divide_by_zero():
    with pytest.raises(ValueError):
        result = my_functions.divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    assert my_functions.divide(10, 5) == 2
    return None

@pytest.mark.skip(reason="This feature is currently broken")
def test_add_skip():
    assert my_functions.add(1,2) == 3

@pytest.mark.xfail(reason="we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(4,0)