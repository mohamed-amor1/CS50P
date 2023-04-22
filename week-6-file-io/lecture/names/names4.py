# open the file called "names.txt" in read mode using a "with" statement
# the "with" statement automatically closes the file after the block of code is executed
with open("names.txt", "r") as file:
    # read all the lines in the file into a list of strings
    # each string represents a single line from the file
    lines = file.readlines()

# iterate over each line in the list of strings
for line in lines:
    # print a greeting message, addressing the person by their name
    # the string is formatted using an "f-string" that includes the name from the file
    # the "rstrip()" method is called on the line to remove any trailing whitespace (such as a newline)
    print(f"hello, {line.rstrip()}")
