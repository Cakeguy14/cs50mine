import sys

def main():
    names = []

    while True:
        try:
            names.append(input("Enter: "))
        except EOFError:
            break

    print(adieu(names))

def adieu(names):
    if len(names) == 1:
        return f"\nAdieu,adieu, to {names[0]}"
    elif len(names) == 2:
        return f"\nAdieu, adieu, to {names[0]} and {names[1]}"
    else:
        all_but_last = ", ".join(names[:-1])
        return f"\nAdieu, adieu, to {all_but_last} and, {names[-1]}"

main()
