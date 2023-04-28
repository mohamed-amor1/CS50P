# enumerate


# Define a list of students
students = ["Hermione", "Harry", "Ron"]

# Loop through the students using the built-in `enumerate` function
# which allows us to iterate over the list and get the index of each element
for i, student in enumerate(students):
    # Print the index of the student plus 1 (to make it start at 1 instead of 0) and the student's name
    print(i + 1, student)
