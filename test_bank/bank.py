class bank:
    def hello(self, greet):
        if greet.startswith("hello"):
            return "$0"
        elif greet.startswith("h"):
            return "$20"
        else:
            return "$100"


def main():
    greeting = input("say something: ").strip().lower()
    account = bank()
    say = account.hello(greeting)
    print(say)

if __name__ == "__main__":
    main()

