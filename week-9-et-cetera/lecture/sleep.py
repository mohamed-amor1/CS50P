# generators, yield


# Define the main function that asks for user input and prints the result
def main():
    # Ask the user for input
    n = int(input("What's n? "))
    # Loop through the result of the sheep generator and print each string
    for s in sheep(n):
        print(s)


# Define the sheep generator function that yields a string of sheep emojis
def sheep(n):
    # Loop through the range of numbers from 0 up to n-1
    for i in range(n):
        # Yield a string of i sheep emojis
        yield "🐑" * i


# Only run the main function if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
