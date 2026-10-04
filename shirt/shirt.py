

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
        PIL.ImageOps.fit(image: photo1, size: tuple[int, int], method: int = Resampling.BICUBIC, bleed: float = 0.0, centering: tuple[float, float] = (0.5, 0.5)) → Image
    return photo1

def ph
