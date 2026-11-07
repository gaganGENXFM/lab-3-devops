import pytest

from calculator import add, divide, multiply, subtract


def test_addition():
    assert add(2, 3) == 5


def test_subtraction():
    assert subtract(5, 3) == 2


def test_multiplication():
    assert multiply(2, 3) == 6


def test_division():
    assert divide(6, 3) == 2


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
