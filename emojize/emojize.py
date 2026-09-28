import emoji

def main():

    text = (input("INPUT: "))
    print(f"OUTPUT: {emoji.emojize(text, language="alias")}")

main()


