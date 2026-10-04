

from PIL import Image
import sys



def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments in command line")

    if not sys.argv[1].endswith(".jpeg") or not sys.argv[2].endswith(".jpeg"):
        sys.exit("Not a jpeg file")
    elif not sys.argv[1].endswith(".png") or not sys.argv[2].endswith(".png"):
        sys.exit("Not a png file")



def photo(filename):
    with Image.open(filename) as photo1:
        
