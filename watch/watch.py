import re
import sys


def main():
    print(parse(str(input("HTML: "))))


def parse(s):
    with open(s) as link:
        iframe = re.search(r'<iframe[^>]*src="([^"]+)"', link)
        if not iframe:
            return None

        string = iframe.group(1)

        parts = string.split("/")
        value = part[-1]
        return f"https://youtu.be/{value}"

if __name__ == "__main__":
    main()
