import sys

# Initialize count variable to 0
count = 0

# Check if the number of command-line arguments is 2 and the second argument is a Python file
if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    # Print the name of the Python file
    print(f"Number of lines in {sys.argv[1]}:")

    try:
        # Open the file in read-only mode and iterate over its lines
        with open(sys.argv[1], "r") as file:
            for line in file:
                # Strip leading whitespace and check if the line is not a comment or a blank line
                if line.strip() and not line.lstrip().startswith("#"):
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Print the count of non-blank non-comment lines
    print(count)

# Check if the number of command-line arguments is 2 but the second argument is not a Python file
elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

# Check if the number of command-line arguments is less than 2
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# Check if the number of command-line arguments is greater than 2
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
