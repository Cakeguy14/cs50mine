def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except (ZeroDivisionError, ValueError):
            pass
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y or x < 0 or y < 0:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 10:
        return "E"
    elif percentage >= 90:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
