
import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments in command line")

    if not sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        sys.exit("Not a csv file")


    try:

    except FileNotFoundError:
        sys.exit("file position is wrong")


def csvread():
    with open(sys.argv[1]) as file1:
        lines = csv.DictReader(file1)
        row = list(lines)
        print(row)
    return row


def csvwrite():
    with open(sys.argv[2], "a", newline="") as file2:
        lines = csv.DictWriter(file2, fieldnames=["name","house"])
        lines.writeheader()
        lines.writerow
        for row in lines:
            first, last = lines["name"].split(",")

