import pytest
from plates import is_valid


def test_word():
    assert is_valid("CS50") == False

def test_num():
    assert is_valid("CAT00") == False

def test_decimal():
    assert is_valid("PI3.14") == False

def test_singleletter():
    assert is_valid("H") == False

def test_correct():
    assert is_valid("LAYRUP") == True

