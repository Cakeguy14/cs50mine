

def main():
    while True:
        Item = []
        item = input("Enter Item: ").upper()
        Item.append(item)

        for i, each in enumerate(Item):
            print(len(i), each)
            pass

        if item == EOFError:
            break

main()

