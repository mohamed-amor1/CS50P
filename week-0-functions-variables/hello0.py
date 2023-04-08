# Ask user for their name
name = input("What's your name? ").strip().lower().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}!")

# Use an f-string to print a message that includes the values of the name and age variables
# The expressions inside the curly braces {} are evaluated at runtime and then inserted into the string
