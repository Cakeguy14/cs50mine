import re
import datetime as dt


def main():
    dates = input("Date of Birth: ")
    print(takedate(dates))


def takedate(value):
    try:
        match = re.fullmatch(r"^([\d{4}])-([\d{2}])-([\d{2}])$", value)
        if match:
            dates = dt.date.fromisoformat(str(value))
            print(dates)
            return dates
    except ValueError:
        sys.exit("Not correct format")

#def convert(value):
    #try:


if __name__ == "__main__":
    main()
