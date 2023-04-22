# Prompt the user to input their name
name = input("What's your name? ")

# Open a new file called "names.txt" in write mode
file = open("names.txt", "w")

# Write the user's name to the file using the .write() method
file.write(name)

# Close the file to release system resources using the .close() method
file.close()
