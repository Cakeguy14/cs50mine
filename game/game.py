import random


def main():
    while True:
        try:
            level = int(input("Level: "))
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

            if guess < value:
                print("Too Small!")
            elif guess > value:
                print("Too Large!")
            else:
                print("Just right!")
                break

        except ValueError:
            pass

main()



