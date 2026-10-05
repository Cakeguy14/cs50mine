import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    with open(s) as link:
        iframe = re.search(r'<iframe[^>]*src, link)
        string = str(youtube.group(1))
        if string:
            for n in string:
                if n == "/":
                    n.split()
                    print("/".join(n))

if __name__ == "__main__":
    main()


<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
