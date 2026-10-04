

from PIL import Image
import sys



def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments in command line")

    valid = (".jpg",".png",".jpeg")

    input_ext = os.path.splittext(sys.argv[1])[1].lower()
    output_ext = os.path.splittext(sys.argv[2])[1].lower()

    if inout_ext not in valid:
        sys.exit("Not a jpeg file")
    elif not sys.argv[1].endswith(".png") or not sys.argv[2].endswith(".png"):
        sys.exit("Not a png file")


    try:
        photo = Image.Open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("file is incorrect")


    shirt = Image.Open("took.png")

