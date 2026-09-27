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

    if dates.isalpha():
        format_two = re.split(r"^([a-zA-Z ])([0-9])\,((\d+){,4})$", ",", date)
        datelist = []
        datelist.append(format_two.group(1)).strip()
        if datelist[i] in Month and format_two.group(2) <= 31:
            print(f"{format_two.group(3)}-{datelist[i]+1}-{format_two.group(2)}")
    elif dates.isalnum() and format_two.group(2) <= 31:
        format_one = re.fullmatch(r"^(\d+){,2}\/(\d+){,2}\/(\d+){,4}$", date)
        print(f"{format_one(3)}-{format_one(2)}-{format_one(1)}")

main()







