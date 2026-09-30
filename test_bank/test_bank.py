import pytest
from bank import hello


def main():
    greet = input("value: ")
    print(test_hello(greet))



def test_hello(greeting):
    if greeting == "hello":
        assert "$0"
    elif greeting.startswith("h"):
        assert "$20"
    else:
        assert "$100"



if __name__ == "__main__":
    main()
