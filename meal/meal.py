import datetime

def main():
    n = (input("WWhat time is it? "))
    print(convert(n))

def convert(n):
    time = datetime.datetime(n)
    if "7:00 AM" < time < "8:00 AM":
        return "Breakfast time"
    elif "12:00 PM" < time < "13:00 PM":
        return "Lunch time"
    elif "18:00 PM" < time < "19:00 PM":
        return "Lunch time"
    else:
        return None

main()

