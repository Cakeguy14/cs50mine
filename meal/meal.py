import datetime

def main():
    n = (input("WWhat time is it? "))
    result = convert(n)
    if result:
        print(result)

def convert(n):
    time = datetime.datetime.strptime(n, "%H:%M").time()
    if datetime.time(7,0) <= time < datetime.time(8,0):
        return "Breakfast time"
    elif datetime.time(12,0) <= time < datetime.time(13,0):
        return "Lunch time"
    elif datetime.time(18,0) <= time < datetime.time(19,0):
        return "Lunch time"
    return None

main()

