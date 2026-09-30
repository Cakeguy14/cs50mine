from bank import bank.hello


def main():
    greet = input("value: ")
    print(value(greet))



def value(greeting):
    banks = bank()
    assert banks.hello("hello") == "$0"
    assert banks.hello("h") == "$20"
    assert banks.hello() == "$100"



if __name__ == "__main__":
    main()
