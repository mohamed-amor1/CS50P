def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")


def square(n):
    return n * n


def main():
    x = get_integer_input("What's x? ")
    result = square(x)
    print(f"{x} squared is {result}")


if __name__ == "__main__":
    main()
