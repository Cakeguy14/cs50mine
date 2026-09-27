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
            if 1 <= day <=31 and 1 <= month <= 12:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
            else:
                continue
            
        match = re.fullmatch(r"([a-zA-z]+) (\d{1,2})\, (\d{4})", dates)

        month_name = match.group(1)







