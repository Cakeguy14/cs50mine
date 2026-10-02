
def main():




def filenames():
    try:
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            if filename.endswith(".py"):
                 return filename
            else:
                 print("Not a python file")
        else:
             print("Too few command line arguments")
    except :




def check():
            else:






def files(file):
    with open(file) as f:
        for row in f:
            code = re.match(r"^(#|# )|([\#A-Z])), row)
            if row not in code:
                return count(row)

