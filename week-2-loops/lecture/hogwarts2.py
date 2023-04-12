# Dictionaries 'dict'

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    "Luna": "Ravenclaw",
    "Neville": "Gryffindor",
    "Ginny": "Gryffindor",
    "Cedric": "Hufflepuff",
    "Cho": "Ravenclaw",
    "Fred": "Gryffindor",
    "George": "Gryffindor",
}

for student in students:
    print(student, students[student], sep=", ")

# 'for student in students' means that the loop will iterate over the keys in the students dictionary. On each iteration, the variable student will be set to the current key.
# 'students[student]' is the corresponding value (i.e., the Hogwarts house) for that key.
# student in students is used to iterate over the keys in the dictionary, while students[student] is used to access the corresponding value for each key.
