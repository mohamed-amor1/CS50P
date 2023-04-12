def main():
    print_square(3)


def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        print()


# Method 2:
# def print_square(size):
#     for i in range(size):
#         print("#" * size)


main()


# The outer loop iterates over each row of the square, and the inner loop iterates over each brick in the row.
# The print() function is called at the end of the inner loop to move the cursor to the next line after each row is printed.
