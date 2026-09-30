import pytest
from twttr import shorten

def main():
    v = input("Enter: ")
    print(test_shorten(v))


def test_shorten(test):
    if test:
        print(shorten(test))
    else:
        raise AssertionError

main()


