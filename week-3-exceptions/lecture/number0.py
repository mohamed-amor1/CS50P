# ValueError: invalid literal for int() with base 10: 'z'
# In case I input a string or != integer
x = int(input("what's x? "))
print(f"x is {x}")


# 'try-except' block is used to catch and handle errors that might occur during execution.
# This helps make programs more robust and user-friendly.

while True:
    try:
        x = int(input("What's x? "))
        print(f"x is {x}")
        break
    except ValueError:
        print("Oops! That was not a valid integer. Please try again...")
