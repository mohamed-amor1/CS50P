# NameError: name 'x' is not defined
# If user types a string he gets NameError ==> passing a string into an int() function.

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

# Because no matter what, line 10 is going to execute.
print(f"x is {x}")
