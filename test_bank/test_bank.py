import pytest
from bank import value


def test_value():
    assert value("hello") == "$0"

def test_h():
    assert value("h") == "$20"

def others():
    assert value("123") == "$100"
