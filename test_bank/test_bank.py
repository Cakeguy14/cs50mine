import pytest
from bank import hello


def main():
    greeting = input("value: ")
    print(test_value(greeting))



def test_value(greeting):
    assert hello("hello") == "$0"
    assert hello("h") == "$20"
    assert hello() == "$100"



if __name__ == "__main__":
    main()
