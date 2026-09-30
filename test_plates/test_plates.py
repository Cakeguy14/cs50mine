import pytest
from plates import is_valid


def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("AB1234") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True


def test_starts_with_letters():
    assert is_valid("1AB") == False
    assert is_valid("A1") == False
    assert is_valid("50") == False


def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("ABCDEFG") == False


def test_number_placement():
    assert is_valid("CS50P2") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("CS0") == False


def test_alphanumeric():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
