def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if valid := re.search(r"^([a-ZA-Z])*\d+)


main()
