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

    if date.isalpha() in dates:
        format_two = re.split(r"^([a-zA-Z 0-9])\,((\d+){,4})$", ",", date)
        print


    format_one = re.fullmatch(r"^(\d+){,2}\/(\d+){,2}\/(\d+){,4}$", date)
    if date == Month in dates:
        format_two = da



