# Get the expression from the user
expression = input("Expression: ")

# Try to split the expression into three parts (x, y, and z)
try:
    x, y, z = expression.split(" ")
except ValueError:
    # If the input expression is not in the correct format, print an error message and exit
    print("Invalid input expression!")
    exit()

# Perform the appropriate arithmetic operation based on the value of y
if y == "+":
    # If y is "+", add x and z and print the result
    print(float(x) + float(z))
elif y == "*":
    # If y is "*", multiply x by z and print the result
    print(float(x) * float(z))
elif y == "/":
    # If y is "/", divide x by z and print the result rounded to one decimal place
    result = float(x) / float(z)
    print(round(result, 1))
elif y == "-":
    # If y is "-", subtract z from x and print the result
    print(float(x) - float(z))
