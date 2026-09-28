import random


def main():
    while True:
        try:
            level = int(input("Enter: "))
            if level > 0:
                break
        except ValueError:
            pass


    value = random.randint(1,level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue

            if value == guess:
                print("Just right!")
            elif value > guess:
                print("Too Large!")
            else:
                print("Too Small")

        except ValueError:
            break

main()



