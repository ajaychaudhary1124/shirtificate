import sys
from PIL import Image, ImageOps
import os


def main():
    if arg_check() != True:
        sys.exit(arg_check())
    else:
        try:
            fir = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Input does not exist")
        shirt = Image.open("shirt.png")
        size = shirt.size
        fir = ImageOps.fit(fir, size)
        fir.paste(shirt, shirt)
        fir.save(sys.argv[2])
        shirt.close()


def arg_check():
    larg = len(sys.argv)
    if larg < 3:
        return "Too few command-line arguments"
    elif larg > 3:
        return "Too many command-line arguments"
    if larg == 3:
        return issupfile()


def issupfile(fin=sys.argv[1], fout=sys.argv[2]):
    ext, oext = [" ", " "]
    name, ext = os.path.splitext(fin)
    oname, oext = os.path.splitext(fout)
    extensions = [".jpeg", ".jpg", ".png"]
    if ext in extensions and oext in extensions:
        if ext != oext:
            sys.exit("Input and output have different extensions")
        return True
    elif ext in extensions and oext not in extensions:
        sys.exit("Invalid output")
    elif ext not in extensions:
        sys.exit("Invalid output")


if __name__ == "__main__":
    main()
