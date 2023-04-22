import csv

# create an empty list to store the student information
students = []

# open the CSV file containing the student information
with open("students.csv") as file:
    # create a dictionary reader object from the CSV file
    reader = csv.DictReader(file)

    # iterate over each row in the CSV file and add a dictionary with the name and home fields to the students list
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# sort the students list in alphabetical order by the name field of each student dictionary
# use a lambda function to specify the key for sorting
# 'key' takes a student dictionary object as its input and returns the value associated with the key "name".
for student in sorted(students, key=lambda student: student["name"]):
    # print the name and home fields for each student in the sorted list
    print(f"{student['name']} is from {student['home']}")
