# Example dictionary
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    "Neville": "Gryffindor",
}

# Convert dictionary to list of tuples and sort based on keys
sorted_tuples = sorted(students.items())

# Convert sorted list back to dictionary
sorted_students = dict(sorted_tuples)

for student in sorted_students:
    print(f"{student}, House: {sorted_students[student]}")
