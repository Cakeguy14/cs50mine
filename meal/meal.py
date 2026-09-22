import datetime

def main():
    time = (input("WWhat time is it? "))
    n = convert(time)

    if 7 <= n < 8:
        print("Breakfast time")
    elif 12 <= n < 13:
        print("Lunch time")
    elif 18 <= n < 19:
        print("Dinner time")


def convert(time):
    hours, mins = time.spilt(":")
    return int(hours)+int(mins)/60

main()

