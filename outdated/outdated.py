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

    for date in dates:
        

