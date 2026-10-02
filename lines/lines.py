
def main():
    try:
        if len(sys.argv) != 2:
            print("Too few command line arguments")
        elif len(sys.argv) > 2:
            print("Too many arguments in command line")
        elif sys.argv[1]:
            if sys.argv[1].endswith(".py"):
                file = sys.argv[1]
            else:
                 print("Not a python file")

    except IndexError:
        print("file position is wrong")


def files(file):
    with open(file) as f:
        for row in f:
            code = re.match(r"^(#|# )|([\#A-Z])), row)
            if row not in code:
                return count(row)

