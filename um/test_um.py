import pytest
from um import count


def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1


def test_multiple_um():
    assert count("um um") == 2
    assert count("um, um, um") == 3
    assert count("Um, um, UM") == 3


def test_um_with_punctuation():
    assert count("um...") == 1
    assert count("um?") == 1
    assert count("um!") == 1
    assert count("um, hello") == 1
    assert count("hello, um, world") == 1
    assert count("hello, um...") == 1


def test_um_in_sentences():
    assert count("Hello, um, world.") == 1
    assert count("Um, hello, um, world.") == 2
    assert count("This is, um, a test, um.") == 2


def test_no_um():
    assert count("hello") == 0
    assert count("") == 0
    assert count("yummy") == 0
    assert count("album") == 0


def test_um_inside_words():
    assert count("umbrella") == 0
    assert count("album") == 0
    assert count("hum") == 0
    assert count("yum") == 0
    assert count("drum") == 0
    assert count("summer") == 0


def test_um_with_extra_spaces():
    assert count(" um ") == 1
    assert count("  um  ") == 1
    assert count("um  um") == 2


def test_um_case_insensitive():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM, um, Um") == 3
