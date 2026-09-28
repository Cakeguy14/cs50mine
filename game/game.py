import random


def main():
    while True:
        try:
            num = input("Enter: ")
        except:
            if num < 0:
                pass


        value = random.randint(range(n))

        if value == num:
            print("Just right!")
            break
        elif value > num:
            print("Too Large!")
            break
        else:
            print("Too Small")
            break

main()



