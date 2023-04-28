# Define a list of dictionaries representing students and their houses
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

# Use a list comprehension to create a new list of names of Gryffindor students
# The comprehension iterates over the elements in the students list, selects only the dictionaries where the "house" key is "Gryffindor",
# and extracts the "name" key from each of those dictionaries to form a new list of names
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

# Use a for loop to iterate over the sorted list of Gryffindor names
for gryffindor in sorted(gryffindors):
    # Print each name
    print(gryffindor)
