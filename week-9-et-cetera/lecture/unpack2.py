# Define a function that takes variable arguments and keyword arguments
def f(*args, **kwargs):
    # Print the keyword arguments
    print("Named:", kwargs)


# Call the function with keyword arguments
# The keyword arguments are passed using the key=value syntax
# They are collected into a dictionary by the **kwargs syntax
f(galleons=100, sickles=50, knuts=25)
