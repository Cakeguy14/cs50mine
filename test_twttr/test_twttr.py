import pytest
from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello") == "Hll"
    assert shorten("AEIOU") == ""
    assert shorten("rhythm") == "rhythm"

    # Capitalized vowels
    assert shorten("AEIOU") == ""
    assert shorten("Twitter") == "Twttr"
    assert shorten("HELLO") == "HLL"

    # Numbers should be kept
    assert shorten("CS50") == "CS50"
    assert shorten("hello123") == "hll123"

    # Punctuation should be kept
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("What's up?") == "Wht's p?"
