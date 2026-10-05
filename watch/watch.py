import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    with open(s) as link:
        youtube = re.search(r'src="([a-zA-Z0-9\/\:\.]+)"', link)
        string = str(youtube.group(1))
        

if __name__ == "__main__":
    main()


<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
