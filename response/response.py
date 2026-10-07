from validator_collection import validators, checkers, errors


def main():
    mail = input("Mail: ")
    try:
        validators.email(mail)
        print("Valid")
    except errors.InvalidEmailError:
        print("Invalid")


main()
