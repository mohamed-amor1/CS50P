# prompt the user to input their name
name = input("What's your name? ")

# open the file called "names.txt" in append mode using a "with" statement
# the "with" statement automatically closes the file after the block of code is executed
with open("names.txt", "a") as file:
    # write the user's name to the file, followed by a newline character
    # the newline character will ensure that each name is on a new line in the file
    file.write(f"{name}\n")
