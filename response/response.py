import validators


def main():
    mail = input("Mail: ")
    try:
        result = validators.email("someone@example.com")
        if result == mail:
            print("Valid")
    elif:

