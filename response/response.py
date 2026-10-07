from validator_collection import validators, checkers, errors


def main():
    mail = input("Mail: ")
    try:
        result = validators.email("someone@example.com")
        if mail:
            value = checkers.is_email(mail)
            print("Valid")
    except errors.InvalidEmailError:
        print("Invalid")


main()
