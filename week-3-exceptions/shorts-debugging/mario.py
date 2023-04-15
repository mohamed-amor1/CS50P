def main():
    height = int(input("Height: "))
    pyramid(height)
    pyramid_2(height)


def pyramid(n):
    for i in range(n):
        # range() function returns a list of integers from some lower bound (zero, by default) up to (but not including) some upper bound (n)
        # We added +1 to i so that it starts from 1 and prints one # in the first line of output
        print("#" * (i + 1))


def pyramid_2(n):  # define a function called 'pyramid_2' that takes one parameter 'n'
    for i in range(n):  # loop through numbers 0 to n-1
        # on each iteration, print a string with n-i-1 spaces " " followed by i+1 hash "#" characters
        print(" " * (n - i - 1) + "#" * (i + 1))


if __name__ == "__main__":
    main()
