from collections import Counter

def main():
    items = []
    while True:
        try:
            item = input(, end="\n").upper()
        except EOFError:
            break

        items.append(item)

    counts = Counter(items)

    for item, count in sorted(counts.items()):
        print(count, item)


main()

