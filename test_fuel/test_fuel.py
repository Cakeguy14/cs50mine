import pytest
from fuel import gauge,convert


def test_convert(x, y):
    assert convert(1/0) == ZeroDivisionError
    assert convert(x) > convert(y) == ValueError
    assert convert(x) < 0 == ValueError
    assert convert(y) < 0 == ValueError

def test_percentage(percentage):
    assert gauge(percentage) >= 90 == "F"
    assert gauge(percentage) <= 10 == "E"
