
def main():
     



def filenames(filename):
    try:
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            if filename.endswith(".py"):



def check():
            else:
                print("Too few command line arguments")





def files(file):
    with open(file) as f:
        for row in f:
            code = re.match(r"^(#|# )|([\#A-Z])), row)
            if row not in code:
                return count(row)

