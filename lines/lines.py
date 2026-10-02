import re
import sys

def main():
    try:
        if len(sys.argv) != 3:
            sys.exit("Too few command line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many arguments in command line")
        elif sys.argv[1]:
            if sys.argv[1].endswith(".py"):
                file = sys.argv[1]
            else:
                 sys.exit("Not a python file")

        print(files(file))

    except IndexError:
        sys.exit("file position is wrong")


def files(file):
    with open(file) as f:
        for row in f:
            code = re.match(r"^(#|# )|([\#a-zA-Z0-9]))", row)
            if row not in code:
                return count(row)


