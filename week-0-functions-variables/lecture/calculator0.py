# A while loop is used to prompt the user for input until valid numbers are entered for both x and y.
while True:
    x = input("What's x? ")
    # The input is attempted to be converted to a float value.
    try:
        x = float(x)
        # If the conversion is successful, the loop is broken and the next input prompt is displayed.
        break
    # If the conversion raises a ValueError exception, an error message is displayed and the loop repeats.
    except ValueError:
        print("Enter a valid number")

while True:
    y = input("What's y? ")
    # The input is attempted to be converted to a float value.
    try:
        y = float(y)
        # If the conversion is successful, the loop is broken and the next line of code is executed.
        break
    # If the conversion raises a ValueError exception, an error message is displayed and the loop repeats.
    except ValueError:
        print("Enter a valid number")

z = round(x/y, 2)
# The values of x and y are added together and the result is printed to the console.
print(f"{x} / {y} = {z}")


# '{z:,}' format the value of the z variable as a string with a comma separating every three digits, making it more readable for users.

# The second argument '2' passed to the round(x/y, 2) function specifies the number of decimal places to round the result of x/y to.
# or we can simply do : print(f"{x} / {y} = {z:.2f}") without adding the '2' argument to the round()function.
