
def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError
            if x > y or x < 0 or y < 0:
                raise ValueError

            percentage = round((x/y)*100)

            if percentage <= 10:
                print("E")
            elif percentage >= 90:
                print("F")
            else:
                print(f"Percentage: {percentage}%")

            break

        except(ZeroDivisionError,ValueError):
            pass

main()

