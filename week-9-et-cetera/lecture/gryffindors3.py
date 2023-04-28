# List of names
students = ["Hermione", "Harry", "Ron"]

# Dictionary comprehension
gryffindors = {student: "Gryffindor" for student in students}

# Print the resulting dictionary
print(gryffindors)


"""We use dictionary comprehension to create a dictionary called gryffindors, which has the names of the students list as its keys, and the string "Gryffindor" as its value for each key.

The syntax for a dictionary comprehension is {key_expression: value_expression for item in iterable}. 

In our case, the key_expression is student, and the value_expression is "Gryffindor".

The for loop specifies the iterable to use, which is the students list in this case.

The dictionary comprehension iterates through each name in the students list, creates a key-value pair in the gryffindors dictionary for each name, and assigns the string "Gryffindor" as the value for each key.

"""
