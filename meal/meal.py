import datetime

def main():
    time = (input("WWhat time is it? "))
    


def convert(time):
    hours, mins = time.spilt(":")
    return int(hours)+int(mins)/60

main()

