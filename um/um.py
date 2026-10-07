import re


def main():
    counts = input("Text: ")
    if counts:
        print(count(counts))

def count(s):
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))

if __name__ == "__main__":
    main()
