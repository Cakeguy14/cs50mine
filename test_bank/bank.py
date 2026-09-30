def main():
    greeting = input("say something: ").strip().lower()
    say = hello(greeting)
    print(say)


def hello(greet):
    if greet.startswith("hello"):
        return "$0"
    elif greet.startswith("h"):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()

