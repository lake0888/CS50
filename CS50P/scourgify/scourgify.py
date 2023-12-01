import sys
import csv

def main():
    if len(sys.argv) == 3:
        before_file = sys.argv[1]
        after_file = sys.argv[2]
        if before_file.endswith("csv") and after_file.endswith("csv"):
            try:
                students = []
                with open(before_file, "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        fullname = row["name"]
                        house = row["house"]

                        last_name, first_name = fullname.strip().split(",")
                        students.append({
                            "first" : first_name.strip(),
                            "last" : last_name,
                            "house" : house
                        })

                with open(after_file, 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for student in students:
                        writer.writerow({
                            "first": student["first"],
                            "last": student["last"],
                            "house": student["house"]
                            })
            except FileNotFoundError:
                sys.exit("Could not read " + before_file)
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()