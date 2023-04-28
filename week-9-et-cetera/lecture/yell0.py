# map


# Define the main function
def main():
    # Call the yell function with some arguments
    yell("This", "is", "CS50")


# Define the yell function that takes variable arguments
def yell(*words):
    # Use the map function to apply the str.upper function to each element in the words tuple
    # The result is an iterator of uppercased strings
    uppercased = map(str.upper, words)

    # Use the print function to output the uppercased words
    # The * operator is used to unpack the iterator as arguments to the print function
    print(*uppercased)


# If this module is executed directly, call the main function
if __name__ == "__main__":
    main()
