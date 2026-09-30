import pytest
from bank import value


def test_value():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello, newman") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Howdy") == 20

def others():
    assert value("what's up") == 100
    assert value("good morning") == 100
