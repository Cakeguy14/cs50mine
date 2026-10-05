import re
import sys


def main():
    print(parse(str(input("HTML: "))))


def parse(s):
    if s:
        iframe = re.search(r'<iframe[^>]*src="([^"]+)"', s)
        if not iframe:
            return None

        string = iframe.group(1)

        parts = string.split("/")
        value = parts[-1]
        if "\" not in value:
            return f"https://youtu.be/{value}"

if __name__ == "__main__":
    main()
