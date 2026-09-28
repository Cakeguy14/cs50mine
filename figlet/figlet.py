
import pyfiglet
import random
import sys

def main():
    fonts = pyfiglet.FigletFont.getFonts()

    if len(sys.argv) == 1 and sys.argv[0] == "figlet.py":
        word = str(input("Enter: "))
        font = random.choice(fonts)
        fig1 = pyfiglet.figlet_format(word, font)
        print(fig1)

    elif len(sys.argv) == 3 and sys.argv[1] in ("-f","-font"):
        word = str(input("Enter: "))
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Not valid")
        else:
            fig = pyfiglet.figlet_format(word, font=font)
            print(fig)

    else:
        sys.exit("The word is not correct")

main()




