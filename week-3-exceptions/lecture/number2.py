# else block is part of try-except statement that gets executed only when no exception is raised in the try block.
# It is a way to handle code that should be executed only if no exceptions occur in the try block.

try:
    x = int(input("What's x?: "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
