def main():
    height = int(input("Height: "))
    pyramid(height)
    pyramid_2(height)


def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))


def pyramid_2(n):  # define a function called 'pyramid_2' that takes one parameter 'n'
    for i in range(n):  # loop through numbers 0 to n-1
        # on each iteration, print a string with n-i-1 spaces " " followed by i+1 hash "#" characters
        print(" " * (n - i - 1) + "#" * (i + 1))


if __name__ == "__main__":
    main()
