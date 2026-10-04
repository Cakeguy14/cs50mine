
import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments in command line")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a csv file")


students = []

def csvread():
    with open(sys.argv[1]) as file1:
        lines = csv.DictReader(file1)
        for row in lines:
            students.append({"name": row["name"], "home": row["home"]})


def csvwrite():
    with open(sys.argv[2], "w", newline="") as file2:
        lines = csv.DictWriter(file2, fieldnames=["first","last","house"])
        lines.writeheader()
        for student in students:
            first, last = student["name"].split(",")
            lines.writerow({"first": first,"last": last, "house": students["house"]})
        print(lines)


if __name__ == "__main__":
    main()

