import sys
from collections import Counter

def main():
    items = []
    while True:
        try:
            print("Item: ", end="", file=sys.stderr)
            item = input().upper()
        except EOFError:
            break

        items.append(item)

    counts = Counter(items)

    for item, count in sorted(counts.items()):
        print(count, item)


main()

