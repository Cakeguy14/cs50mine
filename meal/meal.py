import datetime

def main():
    n = datetime(input("WWhat time is it? "))
    print(convert(n))

def convert(n):
    time = datetime.time(n)
    if time > "7:00 AM":
        return f"{time}

