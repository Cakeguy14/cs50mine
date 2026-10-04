
import os
from PIL import Image, ImageOps
import sys



def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments in command line")

    valid = (".jpg",".png",".jpeg")

    input_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_ext = os.path.splitext(sys.argv[2])[1].lower()

    if input_ext not in valid:
        sys.exit("Not a a correct file")
    if output_ext not in valid:
        sys.exit("Not a a correct file")
    if input_ext != output_ext:
        sys.exit("Not same file format")


    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("file is incorrect")


    shirt = Image.open("shirt.png")

    photo = ImageOps.fit(photo, shirt.size)

    photo.paste(shirt, shirt)

    photo.save(sys.argv[2])

if __name__ == "__main__":
    main()


