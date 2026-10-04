
import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments in command line")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a csv file")



    students = csvread(sys.argv[1])
    csvwrite(sys.argv[2], students)



def csvread(filename):
    students = []
    try:
        with open(filename) as file1:
            lines = csv.DictReader(file1)
            for row in lines:
                students.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File position not correct")
    return students


def csvwrite(filename, students):
    with open(filename, "w", newline="") as file2:
        lines = csv.DictWriter(file2, fieldnames=["first","last","house"])
        lines.writeheader()
        for student in students:
            first, last = student["name"].split(",")
            lines.writerow({"first": first,"last": last, "house": student["house"]})


if __name__ == "__main__":
    main()

