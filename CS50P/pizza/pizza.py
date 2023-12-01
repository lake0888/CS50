import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
        if not fileName.endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            try:
                header = ["Regular Pizza", "Small", "Large"]
                if fileName.startswith("sicilian"):
                    header[0] = "Sicilian Pizza"

                pizza = []
                with open(fileName, "r") as file:
                    reader =  csv.DictReader(file)
                    for row in reader:
                        pizza.append([row[header[0]], row[header[1]], row[header[2]]])
                    print(tabulate(pizza, header, tablefmt="grid"))
            except FileNotFoundError:
                sys.exit("File does not exist")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()