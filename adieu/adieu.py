

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
        print (f"Adieu,adieu, to {names[0]}")
    elif len(names) == 2:
        print (f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        all_but_last = ", ".join(names[:-1])
        print (f"Adieu, adieu, to {all_but_last} and {name[:-1]}")

main()



