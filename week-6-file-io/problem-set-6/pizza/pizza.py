import csv
import sys
from tabulate import tabulate

# Create an empty list to store the rows of the CSV file
table = []

# Check if the number of command-line arguments is 2 and the second argument is a CSV file
if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
    try:
        # Open the CSV file in read-only mode and iterate over its rows
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)

        # Print the table of CSV data using tabulate
        print(tabulate(table, headers="keys", tablefmt="mixed_grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

# Check if the number of command-line arguments is 2 but the second argument is not a CSV file
elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

# Check if the number of command-line arguments is greater than 2
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check if the number of command-line arguments is less than 2
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
