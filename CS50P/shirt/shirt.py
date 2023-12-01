import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3:
        file_input = sys.argv[1]
        file_output = sys.argv[2]

        if not file_input.endswith(".jpg") and not file_input.endswith(".jpeg") and not file_input.endswith(".png"):
            sys.exit("Invalid input")
        elif not file_output.endswith(".jpg") and not file_output.endswith(".jpeg") and not file_output.endswith(".png"):
            sys.exit("Invalid output")
        else:
            try:
                name_input, extension_input = file_input.rsplit(".", 1)
                name_output, extension_output = file_output.rsplit(".", 1)

                if extension_input != extension_output:
                    sys.exit("Input and output have different extensions")

                image_input = Image.open(file_input)
                shirt = Image.open("shirt.png")
                image_output = ImageOps.fit(image_input, shirt.size)
                image_output.paste(shirt, shirt)
                image_output.save(file_output)

            except ValueError:
                sys.exit("Invalid files")
            except FileNotFoundError:
                sys.exit("Input does not exist")


    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()