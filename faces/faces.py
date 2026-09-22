def main():
    word = str(input("Enter your comment: "))
    convert(word)


def convert(n):
       while True:
            has_hello = "Hello :)" in n
            has_goodbye = "Goodbye :(" in n
            if has_hello and has_goodbye:
                 print (f"Hello 🙂 Goodbye 🙁")
                 break
            elif has_hello:
                print (f"Hello 🙂")
                break
            elif has_goodbye:
                print (f"Goodbye 🙁")
                break
            else:
                print("enter correct values")
                break

if __name__ == "__main__":
    main()


