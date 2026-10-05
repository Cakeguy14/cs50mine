import re


def main():
    value = str(input("HTML: "))
    if value:
        print(parse(value))

def parse(s):
    src = re.search(r'src="([^"]+)"', s)
    if not src:
        None

    url = src.group(1)

    return url


if __name__ == "__main__":
    main()
