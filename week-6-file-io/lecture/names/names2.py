# prompt the user to input their name
name = input("What's your name? ")

# open the file called "names.txt" in append mode
# this will allow us to add the user's name to the end of the file
file = open("names.txt", "a")

# write the user's name to the file, followed by a newline character
# the newline character will ensure that each name is on a new line in the file
file.write(f"{name}\n")

# close the file to release system resources
file.close()
