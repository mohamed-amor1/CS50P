# The 'prompt' parameter is used instead of just prompting the user through the input() function inside the get_int() function to make the function more flexible and reusable.
# By using a prompt parameter, the function can be used to get integer input with different prompts in different parts of the program without duplicating code.


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # The 'pass' keyword is used to indicate that there is no action to be taken if an exception of type ValueError is raised.
            pass
            # 'pass' in indented inside except because we want to pass only when a ValueError is raised.


main()
