import re
import datetime as dt


def main():
    dates = input("Date of Birth: ")
    print(takedate(dates))


def takedate(value):
    try:
        match = re.search(r"^\d{4}-\d{2}-\d{2}$", value)
        if match:
            dates = dt.date.fromisoformat(value)
        return dates
    except ValueError:
        sys.exit("Not correct format")

def convert(value):
    try:
        words = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", value)
        word1 = words.group(1)
        word2 = words.group(2)
        word3 = words.group(3)
        



if __name__ == "__main__":
    main()
