import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments in command line")

    file = sys.argv[1]
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as f:
            lines = csv.DictReader(f)
            row = list(lines)

    except FileNotFoundError:
        sys.exit("file position is wrong")

    print(tabulate(row, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
