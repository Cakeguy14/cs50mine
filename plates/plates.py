import re

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not re.match(r"^[a-zA-Z]{2,}", s):
        return False
    if not re.match(r"^[a-zA-Z0-9]+$", s):
        return False
    if re.search(r"[a-zA-Z][0-9]", s):
        return False
    if re.search(r"0[0-9]", s):
        return False

    return True



main()
