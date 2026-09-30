import pytest
from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello") == "Hll"
    assert shorten("AEIOU") == ""
    assert shorten("rhythm") == "rhythm"

    assert shorten("AEIOU") == ""
    assert shorten("Twitter") == "Twttr"
    assert shorten("HELLO") == "HLL"

    assert shorten("CS50") == "CS50"
    assert shorten("hello123") == "hll123"

    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("What's up?") == "Wht's p?"
