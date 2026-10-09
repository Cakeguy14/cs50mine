import re
from datetime import date


def main():
    dates = input("Date of Birth: ")
    print(takedate(dates))


def takedate(value):
    try:
        match = re.fullmatch(r"^([\d{4}])-([\d{2}])-([\d{2}])$", value)
        if match:
            dates = date.date.fromisoformat(str(value))
            return dates
    except ValueError:
        sys.exit("Not correct format")


if __name__ == "__main__":
    main()
