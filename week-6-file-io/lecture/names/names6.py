# create an empty list to store the names
names = []

# open the file called "names.txt" in read mode using a "with" statement
# the "with" statement automatically closes the file after the block of code is executed
# if the mode is not specified, "r" mode (read mode) is used by default
with open("names.txt") as file:
    # iterate over each line in the file
    # the "for" loop automatically reads one line at a time from the file
    for line in file:
        # remove any trailing whitespace (such as a newline) from the line, and append it to the "names" list
        names.append(line.rstrip())


# iterate over each name after sorting names list
for name in sorted(names):
    # print a greeting message, addressing the person by their name
    # the string is formatted using an "f-string" that includes the name from the list
    print(f"hello, {name}")
