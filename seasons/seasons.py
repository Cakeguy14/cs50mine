import re
import datetime as dt
import sys
import inflect


def main():
    dates = input("Date of Birth: ")
    try:
        birth = convert(dates)
    except ValueError:
        sys.exit("Invalid date")

    p = inflect.engine()
    value = p.number_to_words(birth, andword="")
    print(f"{value.capitalize()} minutes")


def convert(value):
    if not re.fullmatch(r"^(\d{4})-(\d{2})-(\d{2})$", value):
        raise ValueError("not correct")

    birth = dt.date.fromisoformat(value)
    date = dt.date.today()
    delta = date - birth

    return abs(delta.days) * 24 * 60


if __name__ == "__main__":
    main()
