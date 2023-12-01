import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
    else:
        # TODO: Read database file into a variable
        database = []
        file_database = sys.argv[1]

        is_large = file_database.find("large.csv") != -1

        sequences = ["AGATC", "AATG", "TATC"]
        if is_large:
            sequences = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]

        with open(file_database, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]

                person = {}
                person["name"] = name

                for dna_sequence in sequences:
                    person[dna_sequence] = int(row[dna_sequence])

                database.append(person)

        # TODO: Read DNA sequence file into a variable
        file_sequence = sys.argv[2]
        file = open(file_sequence, "r")
        sequence = file.read()

        # TODO: Find longest match of each STR in DNA sequence
        result = {}
        for dns_sequence in sequences:
            result[dns_sequence] = longest_match(sequence, dns_sequence)

        # TODO: Check database for matching profiles
        dna_name = "No match"
        for i in range(len(database)):
            current = database[i]
            name = current["name"]

            match = 0
            for dns_sequence in sequences:
                if current[dns_sequence] == result[dns_sequence]:
                    match += 1

            if match == len(sequences):
                dna_name = name
                break

        print(dna_name)

        return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
