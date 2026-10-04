

from PIL import Image
import sys



def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments in command line")

    if not sys.argv[1].endswith(".jpg") or not sys.argv[2].endswith(".jpg"):
        sys.exit("Not a jpg file")
    elif not sys.argv[1].endswith(".png") or not sys.argv[2].endswith(".png"):
        sys.exit("Not a png file")
