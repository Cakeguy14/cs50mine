def main():
    name = input("File name: ").strip().lower()
    print(filename(name))

def filename(name):
    if name.endswith(".gif"):
        return "image/gif"
    elif name.endswith(".png"):
        return "image/png"
    elif name.endswith(".jpg") or name.endswith(".jpeg"):
        return "image/jpeg"
    elif name.endswith(".txt"):
        return "text/plain"
    elif name.endswith(".pdf"):
        return "application/pdf"
    elif name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()
