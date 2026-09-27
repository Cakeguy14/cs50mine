import re


Month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            dates = input("DATE: ")
        except:
            raise ValueError("Date is not correct format")
        break

    dates = []

    format_one = re.fullmatch(r"^(\d+){,2}\/(\d+){,2}\/(\d+){,4}$", date)
    if date == Month in dates:
        format_two = da



