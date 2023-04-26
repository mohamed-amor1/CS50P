# In Python, a tuple is an ordered, immutable sequence of elements.
# Once a tuple is created, its values cannot be modified.
# Tuples are commonly used to store related pieces of data that shouldn't be modified,
# such as a set of coordinates or a date and time.

# The basic syntax for creating a tuple in Python is to enclose a comma-separated sequence
# of values in parentheses.
my_tuple = (1, 2, 3)

# You can also create a tuple using the built-in `tuple()` function:
my_tuple = tuple([1, 2, 3])

# To access an element of a tuple, you can use indexing, just like with a list:
print(my_tuple[0])  # Output: 1

# You can also use slicing to access a subset of a tuple:
print(my_tuple[1:])  # Output: (2, 3)
