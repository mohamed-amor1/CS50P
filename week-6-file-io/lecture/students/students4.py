# create an empty list to store the student information
students = []

# open the file containing the student information
with open("students.csv") as file:
    # read the file line by line and parse the name and house fields from each line
    for line in file:
        name, house = line.rstrip().split(",")
        # create a dictionary to store the name and house fields for each student
        student = {"name": name, "house": house}
        # add the student dictionary to the students list
        students.append(student)

# sort the students list in alphabetical order by the name field of each student dictionary
# use a lambda function to specify the key for sorting
# 'key' takes a student dictionary object as its input and returns the value associated with the key "name".
for student in sorted(students, key=lambda student: student["name"]):
    # print the name and house fields for each student in the sorted list
    print(f"{student['name']} is in {student['house']}")
