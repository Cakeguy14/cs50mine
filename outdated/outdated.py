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
        dates = input("DATE: ")

        match = re.fullmatch(r"(\d{1,2})\/(\d{1,2})\/(\d{4})", dates)

        if match:
            month = match.group(1)
            day = match.group(2)
            year = match.group(3)
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        else:
            continue

        match

main()







