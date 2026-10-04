import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    src = re.search(r"src=\"([a-ZA-Z0-9\/\.])\"", s)
    if src:
        embed = src.group(1)
    return embed




if __name__ == "__main__":
    main()
