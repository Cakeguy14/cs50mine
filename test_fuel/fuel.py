
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    result = gauge(percentage)
    print(result)


def convert(fraction):
    while True:
          x, y = fraction.split("/")
          x = int(x)
          y = int(y)
          try:
               if y == 0:
                    raise ZeroDivisionError
               if x > y or x < 0 or y < 0:
                    raise ValueError

               percentage = round((x/y)*100)

               return percentage

            except(ZeroDivisionError,ValueError):
               pass
               break


def gauge(percentage):
    if percentage <= 10:
         print("E")
    elif percentage >= 90:
        print("F")
    else:
        print(f"Percentage: {percentage}%")


if __name__ == "__main__":
    main()
