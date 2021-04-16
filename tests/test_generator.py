import unittest

from calculator import sum

def test_sum_simple_numbers():
    numbers = (12, 15)
    result = sum.sum(*numbers)
    assert isinstance(result, int)


def test_sum_float_numbers():
    numbers = (7.14, 4.163)
    result = sum.sum(*numbers)
    assert isinstance(result, float)

