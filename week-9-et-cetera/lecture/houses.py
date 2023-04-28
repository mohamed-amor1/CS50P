# set() vs. list()

# A set is an unordered collection of unique items, meaning each item can only appear once in the set.
# Items in a set are not stored in any particular order, and you can't access them by their index position like you can with a list.


# Creating a list of dictionaries representing students and their houses
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Cedric", "house": "Hufflepuff"},
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Neville", "house": "Gryffindor"},
    {"name": "Pansy", "house": "Slytherin"},
]


# Initializing an empty set to store unique house names
houses = set()

# Iterating over each student in the list
for student in students:
    # Adding the student's house to the set
    houses.add(student["house"])

# Sorting the set of house names and printing them
for house in sorted(houses):
    print(house)

# set: You can add and remove items from a set using the 'add()' and 'remove()' methods, and you can check if an item is in a set using the 'in' keyword.
# list: You can add items to the end of a list using the 'append()' method, or insert them at a specific position using the 'insert()' method. You can also remove items from a list using the 'remove()' method, or remove and return the last item using the 'pop()' method.
