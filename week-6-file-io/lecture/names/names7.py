# Open the file called "names.txt" in read mode using a "with" statement
# If the mode is not specified, "r" mode (read mode) is used by default
with open("names.txt") as file:
    # Read the lines from the file and sort them descending using the `sorted()` function and reverse=True parameter
    # The `sorted()` function returns a new sorted list without modifying the original list
    # The `for` loop iterates over each sorted line in the file
    for line in sorted(file, reverse=True):
        # Remove any trailing whitespace (such as a newline) from the line, and print a greeting message
        # The string is formatted using an "f-string" that includes the name from the line
        print(f"hello, {line.rstrip()}")
