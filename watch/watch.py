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

        pattern = r'^https?://(?:www\.)?(?:youtube\.com/embed/|youtu\.be/)([a-zA-Z0-9_-]+)$'
        match = re.search(pattern, string, re.IGNORECASE)

        if not match:
            return none

        return f"https://youtu.be/{match.group(1)}"

if __name__ == "__main__":
    main()
