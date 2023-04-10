def main():
    while True:
        try:
            x = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


main()
