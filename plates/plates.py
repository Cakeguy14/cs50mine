def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return false
    if not re.match(r"^[a-zA-Z]{2,}", s):
        return false
    if not re.search(r"^[a-zA-Z0-9]+$", s):
        return false
    if re.search(r"[a-zA-Z][0-9]", s):
        return false
    if re.search(r"0[0-9]", s):
        return false
    


main()
