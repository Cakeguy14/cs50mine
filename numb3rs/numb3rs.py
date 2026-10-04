import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    address = ip.split(".")
    num = list(address)
    for n in num:
        if not n.isdigit():
            return False
        if len(n) > 1 and n[0] == "0":
            return False
        if 0 <= int(n) <= 255:
            return False

    return True


if __name__ == "__main__":
    main()
