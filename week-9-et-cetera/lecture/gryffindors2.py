# List of names
students = ["Hermione", "Harry", "Ron"]

# List comprehension to create a list of dictionaries for each student, with the house "Gryffindor"
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# Print the resulting list of dictionaries
print(gryffindors)
