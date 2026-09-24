

def main():
    Item = []
    while True:
        try:
            item = input("Enter Item: ").upper()
        except EOFError:
            break

        Item.append(item)

        for i, each in enumerate(Item):
            print(i, each)

main()

