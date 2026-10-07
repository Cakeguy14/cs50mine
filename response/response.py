import validators


def main():
    mail = input("Mail: ")
    try:
        result = validators.email("someone@example.com")
        if mail:
            value = checkers.is_email(mail)
            print("Valid")
    except NotAnemailError:
        


