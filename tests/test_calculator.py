import pytest
from simple_calculator.calculator import add, multiply, subtract, divide


def test_add_two_positive_numbers():
    """Asserts whether add function can
    successfully add two positive numbers"""
    assert add(82, 91) == 173


def test_add_two_negative_numbers():
    """Asserts whether add function can add
    two negative numbers"""
    assert add(-15, -5) == -20


def test_add_multiple_numbers():
    """Asserts whether add function is
    able to add multiple numbers
    of both negative and positive values."""
    assert add(10, 12, 14, 16, 18) == 70
    assert add(1, 2, 3, -6, 4, -3) == 1


def test_multiply_two_positive_numbers():
    """Asserts whether multiply function
    is able to multiply two positive
    numbers"""
    assert multiply(4, 3) == 12


def test_multiply_one_negative_one_positive_number():
    """Asserts whether multiply function
    can multiple one positive and one
    negative  number"""
    assert multiply(20, -10) == -200


def test_multiply_multiple_numbers():
    """Asserts whether the multiply
    function can multiply multiple
    numbers"""
    assert multiply(1, 2, 3, 4, 5) == 120


def test_subtract_two_positive_numbers():
    """Asserts whether the subtract function
    can subtract two numbers"""
    assert subtract(15, 8) == 7


def test_subtract_two_negative_numbers():
    """Asserts whether subtract function
    can subtract two negative numbers"""
    assert subtract(-10, -20) == -30


def test_subtract_multiple_numbers():
    """Asserst the subtract function
    can subtract multiple numbers"""
    assert subtract(10, 5, 3) == 2


def test_divide_two_numbers():
    '''Assert whether the divide function
    can divide two numbers'''
    assert divide(10,2) == 5


def test_divide_one_negative_one_positive_number():
    '''Assert whether divide function
    can handle division between one
    positive and one negative number'''
    assert divide(10, -50) == -0.20


def test_divide_multiple_numbers():
    '''Assert whether the divide function
    can divide multiple numbers'''
    assert divide(20,-4,-2) == 2.5
