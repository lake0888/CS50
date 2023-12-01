import sys

if len(sys.argv) == 2:
    fileName = sys.argv[1]
    if fileName.endswith(".py"):
        try:
            file = open(fileName, "r")
            number = 0
            for line in file:
                if not line.lstrip().startswith("#") and not line.isspace():
                    number += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            file.close()
            print(number)
    else:
        sys.exit("Not a Python file")
elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")
