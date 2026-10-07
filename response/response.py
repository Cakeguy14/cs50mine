import validators


def main():
    mail = input("Mail: ")
    if mail:
        result = validators.email("someone@example.com")
        if result == mail:
            print("Valid")
    elif:

