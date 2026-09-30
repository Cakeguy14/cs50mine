import pytest
from fuel import convert, gauge


def test_convert_basic():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/4")


def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/2")


def test_gauge_e():
    assert gauge(10) == "E"
    assert gauge(1) == "E"


def test_gauge_f():
    assert gauge(90) == "F"
    assert gauge(99) == "F"


def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
