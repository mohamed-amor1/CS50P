# list comprehensions


# Define the main function
def main():
    # Call the yell function with some arguments
    yell("This", "is", "CS50")


# Define the yell function that takes variable arguments
def yell(*words):
    # Use a list comprehension to create a new list of uppercased words
    # The comprehension iterates over the elements in the words tuple and applies the upper() method to each
    uppercased = [word.upper() for word in words]

    # Use the print function to output the uppercased words
    # The * operator is used to unpack the list as arguments to the print function
    print(*uppercased)


# If this module is executed directly, call the main function
if __name__ == "__main__":
    main()
