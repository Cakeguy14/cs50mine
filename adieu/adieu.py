

def main():
    names = input("Enter: ")

    if len(names) == 1:
        print f"Adieu,adieu, to {names[0]}"
    elif len(names) == 2:
        for name in names:
            print f"Adieu, adieu, to {names[0]} and {names[1]}"
    elif len(names) > 2:
        for name in names:
            print f"Adieu, adieu, to {name} and {name[n-1]}"

main()



