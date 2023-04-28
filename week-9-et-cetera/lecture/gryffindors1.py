# Define a list of dictionaries representing the students and their houses
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

# Use filter() to create an iterator that returns only the students who are in Gryffindor
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

# Sort the list of Gryffindors alphabetically by name and print only the name of each student
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
