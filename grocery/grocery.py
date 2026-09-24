import sys
from collections import Counter

def main():
    items = []
    while True:
        try:
            item = input().upper()
        except EOFError:
            break

        items.append(item)

    counts = Counter(items)

    print()

    for item, count in sorted(counts.items()):
        print(count, item)


main()

