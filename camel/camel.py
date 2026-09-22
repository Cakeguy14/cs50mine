import re

def main():
    case = input("camelCase: ")
    cases = snakecase(case)
    if cases:
        print(cases)


def snakecase(case):
    result = ""
    for i,c in enumerate(case):
        if c.isupper():
            if i > 0:
                result += "_"
            result += c.lower()
        else:
            result += c
    return result


main()
