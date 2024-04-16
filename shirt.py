import sys
from PIL import Image, ImageOps
import os

# Main function of the program
def main():
    # Check if the command-line arguments are valid
    if arg_check() != True:
        sys.exit(arg_check())  # Exit if arguments are not valid
    else:
        try:
            fir = Image.open(sys.argv[1])  # Open the input image
        except FileNotFoundError:
            sys.exit("Input does not exist")  # Exit if input image doesn't exist
        shirt = Image.open("shirt.png")  # Open the shirt image
        size = shirt.size
        fir = ImageOps.fit(fir, size)  # Resize the input image to fit the shirt
        fir.paste(shirt, shirt)  # Paste the shirt image onto the resized input image
        fir.save(sys.argv[2])  # Save the final image
        shirt.close()

# Function to check the number of command-line arguments
def arg_check():
    larg = len(sys.argv)
    if larg < 3:
        return "Too few command-line arguments"
    elif larg > 3:
        return "Too many command-line arguments"
    if larg == 3:
        return issupfile()

# Function to check if the input and output files have valid extensions
def issupfile(fin=sys.argv[1], fout=sys.argv[2]):
    ext, oext = [" ", " "]
    name, ext = os.path.splitext(fin)  # Split input filename and extension
    oname, oext = os.path.splitext(fout)  # Split output filename and extension
    extensions = [".jpeg", ".jpg", ".png"]
    if ext in extensions and oext in extensions:
        if ext != oext:
            sys.exit("Input and output have different extensions")  # Exit if input and output have different extensions
        return True
    elif ext in extensions and oext not in extensions:
        sys.exit("Invalid output")  # Exit if output extension is invalid
    elif ext not in extensions:
        sys.exit("Invalid output")  # Exit if input extension is invalid

# Entry point of the program
if __name__ == "__main__":
    main()
