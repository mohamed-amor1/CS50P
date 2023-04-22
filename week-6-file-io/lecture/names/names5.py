# open the file called "names.txt" in read mode using a "with" statement
# the "with" statement automatically closes the file after the block of code is executed
with open("names.txt", "r") as file:
    # iterate over each line in the file
    # the "for" loop automatically reads one line at a time from the file
    for line in file:
        # print a greeting message, addressing the person by their name
        # the string is formatted using an "f-string" that includes the name from the file
        # the "rstrip()" method is called on the line to remove any trailing whitespace (such as a newline)
        print(f"hello, {line.rstrip()}")
