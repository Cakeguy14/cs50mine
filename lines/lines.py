
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments in command line")

    file = sys.argv[1]
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    try:
        print(files(file))
    except FileNotFoundError:
        sys.exit("file position is wrong")


def files(file):
    count = 0
    with open(file) as f:
        for row in f:
            code = row.strip()
            if code and not code.startswith("#"):
                count += 1
    return count


if __name__ == "__main__":
    main()


