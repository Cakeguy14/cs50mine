import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        correct = a + b


        tries = 0
        while tries < 3:
            try:
                ans = int(input(f"{a}+{b} ="))
                if ans == correct:
                    print()







def get_level(level):
    while True:
        try:
            level = input("LEVEL: ")
            if level in (1,2,3):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,10)
    elif level == 2:
        return random.randint(10, 100)
    elif level == 3:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()
