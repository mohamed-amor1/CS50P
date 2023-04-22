import csv
import sys

# Define the list to store the data from the input CSV file
before = []

# Define the field names to use in the output CSV file
field_names = ["first", "last", "house"]

# Check if two command line arguments have been provided, and both are CSV files
if len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
    try:
        # Read the data from the input CSV file and store it in the before list
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                before.append(row)
    except FileNotFoundError:
        # If the input file is not found, print an error message and exit
        sys.exit(f"Could not read {sys.argv[1]}")

    # Process the data from the input CSV file
    for d in before:
        # Split the 'name' field into 'last' and 'first' fields
        d["last"], d["first"] = d["name"].split(", ")

    try:
        # Write the processed data to the output CSV file
        with open(sys.argv[2], "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            # Write the header row in the output CSV file
            writer.writeheader()
            for row in before:
                # Remove the 'name' field from the dict before writing it to the output CSV file
                row.pop("name")
                writer.writerow(row)
    except FileNotFoundError:
        # If the output file cannot be written, print an error message and exit
        sys.exit(f"Could not write {sys.argv[2]}")

# If the number of command line arguments is not 3, or the arguments are not CSV files, print an error message and exit
elif (
    len(sys.argv) != 3
    or not sys.argv[1].endswith(".csv")
    or not sys.argv[2].endswith(".csv")
):
    sys.exit("Usage: python script.py input.csv output.csv")
