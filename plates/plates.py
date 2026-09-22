def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while len(s) == 6:
        if valid := re.search(r"^([a-ZA-Z])*\d+$", s)
        return valid
    else:
        break

main()
